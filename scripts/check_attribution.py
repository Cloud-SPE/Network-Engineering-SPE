#!/usr/bin/env python3
"""Reject co-author attribution in commit and pull-request messages."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


PROHIBITED = re.compile(
    r"(?im)(?:^|\b)co[ -]?authored[ -]?by\s*:|\bco[ -]?author(?:ed|ship)?\b"
)


def git_messages(revision: str) -> list[str]:
    result = subprocess.run(
        ["git", "log", "--format=%H%x00%B%x00", revision],
        check=True,
        capture_output=True,
        text=True,
    )
    fields = result.stdout.split("\0")
    messages: list[str] = []
    for index in range(0, len(fields) - 1, 2):
        commit = fields[index].strip()
        message = fields[index + 1].strip()
        if commit:
            messages.append(f"commit {commit}:\n{message}")
    return messages


def event_messages(event_file: Path) -> tuple[list[str], str | None]:
    event = json.loads(event_file.read_text(encoding="utf-8"))
    messages: list[str] = []
    revision: str | None = None

    pull_request = event.get("pull_request")
    if pull_request:
        messages.extend(
            [
                f"pull-request title:\n{pull_request.get('title') or ''}",
                f"pull-request body:\n{pull_request.get('body') or ''}",
            ]
        )
        base = pull_request["base"]["sha"]
        head = pull_request["head"]["sha"]
        revision = f"{base}..{head}"
    elif event.get("after"):
        before = event.get("before")
        after = event["after"]
        revision = after if not before or set(before) == {"0"} else f"{before}..{after}"

    return messages, revision


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-history", action="store_true")
    parser.add_argument("--event-file", type=Path)
    args = parser.parse_args()

    messages: list[str] = []
    if args.all_history:
        messages.extend(git_messages("--all"))
    elif args.event_file:
        event_values, revision = event_messages(args.event_file)
        messages.extend(event_values)
        if revision:
            messages.extend(git_messages(revision))
    else:
        parser.error("use --all-history or --event-file")

    violations = [message for message in messages if PROHIBITED.search(message)]
    if violations:
        print("Co-author attribution is prohibited:", file=sys.stderr)
        for violation in violations:
            print(f"\n{violation}", file=sys.stderr)
        return 1

    print(f"Attribution policy passed ({len(messages)} messages checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
