#!/usr/bin/env python3
"""Validate the repository's lightweight documentation contract."""

from __future__ import annotations

import re
import sys
from collections import Counter
from fnmatch import fnmatchcase
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "ARCHITECTURE.md",
    "CONTRIBUTING.md",
    "README.md",
    "docs/index.md",
    "docs/references/index.md",
    "docs/QUALITY.md",
    "docs/design-docs/index.md",
    "docs/product-specs/index.md",
    "docs/decisions/index.md",
)
LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
CATALOG_ROW_RE = re.compile(
    r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*"
    r"\[[^]]+\]\(([^)#]+\.md)(?:#[^)]*)?\)\s*\|",
    re.MULTILINE,
)
LOCAL_ONLY_EVIDENCE_NAMES = (
    "*transcript.txt",
    "*-gemini-*-notes.md",
)


def is_local_only_evidence(path: Path) -> bool:
    reference_root = ROOT / "docs" / "references"
    try:
        path.resolve().relative_to(reference_root)
    except ValueError:
        return False
    name = path.name.lower()
    return any(fnmatchcase(name, pattern) for pattern in LOCAL_ONLY_EVIDENCE_NAMES)


def markdown_files() -> list[Path]:
    excluded = {".git", ".beads", ".agents"}
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in excluded for part in path.relative_to(ROOT).parts)
        and not is_local_only_evidence(path)
    )


def local_target(raw_target: str) -> str | None:
    target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    return unquote(target.split("#", 1)[0])


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    files = markdown_files()
    for path in files:
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        h1_count = sum(line.startswith("# ") for line in text.splitlines())
        if h1_count != 1:
            errors.append(f"{relative}: expected exactly one H1, found {h1_count}")

        for match in LINK_RE.finditer(text):
            target = local_target(match.group(1))
            if target is None:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: link escapes repository: {target}")
                continue
            if is_local_only_evidence(resolved):
                errors.append(
                    f"{relative}: link targets local-only evidence: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(f"{relative}: broken local link: {target}")

    reference_root = ROOT / "docs" / "references"
    reference_index = reference_root / "index.md"
    reference_files = {
        path.resolve()
        for path in files
        if reference_root in path.parents and path != reference_index
    }

    for path in sorted(reference_files):
        if not DATE_PREFIX_RE.match(path.name):
            errors.append(
                f"{path.relative_to(ROOT)}: reference filename needs YYYY-MM-DD prefix"
            )

    if reference_index.is_file():
        catalog_text = reference_index.read_text(encoding="utf-8")
        catalog_rows = CATALOG_ROW_RE.findall(catalog_text)
        catalog_dates = [date for date, _ in catalog_rows]
        catalog_paths: list[Path] = []

        for date, raw_target in catalog_rows:
            resolved = (reference_index.parent / raw_target).resolve()
            catalog_paths.append(resolved)
            if resolved.name[:10] != date:
                errors.append(
                    f"docs/references/index.md: catalog date {date} does not "
                    f"match filename {resolved.name}"
                )

        if catalog_dates != sorted(catalog_dates, reverse=True):
            errors.append(
                "docs/references/index.md: chronological catalog must be newest first"
            )

        counts = Counter(catalog_paths)
        for path in sorted(reference_files - set(catalog_paths)):
            errors.append(
                f"docs/references/index.md: missing reference: "
                f"{path.relative_to(reference_root)}"
            )
        for path in sorted(set(catalog_paths) - reference_files):
            errors.append(
                f"docs/references/index.md: catalog target is not a reference: "
                f"{path.relative_to(ROOT)}"
            )
        for path, count in sorted(counts.items()):
            if count > 1:
                errors.append(
                    f"docs/references/index.md: reference listed {count} times: "
                    f"{path.relative_to(reference_root)}"
                )

    if errors:
        print("Documentation checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Documentation checks passed ({len(files)} Markdown files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
