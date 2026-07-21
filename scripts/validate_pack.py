#!/usr/bin/env python3
"""Validate that a Context Passport or Agent Handoff file has key sections."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_SECTIONS = {
    "context-passport": [
        "Purpose",
        "Original Goal",
        "Current Status",
        "Decisions",
        "Open Questions",
        "Next Actions",
        "Resume Prompt",
    ],
    "agent-handoff": [
        "Objective",
        "Current Status",
        "Completed",
        "Pending",
        "Key Decisions",
        "Next Actions",
        "Resume Prompt",
    ],
}


def has_heading(text: str, heading: str) -> bool:
    return f"## {heading}" in text or f"# {heading}" in text


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a context handoff Markdown file.")
    parser.add_argument("path", help="Markdown file to validate")
    parser.add_argument(
        "--kind",
        choices=sorted(REQUIRED_SECTIONS),
        default="context-passport",
        help="Template kind to validate against",
    )
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    missing = [section for section in REQUIRED_SECTIONS[args.kind] if not has_heading(text, section)]

    if missing:
        print(f"{path}: missing sections: {', '.join(missing)}")
        return 1

    print(f"{path}: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

