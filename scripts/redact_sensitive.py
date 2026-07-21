#!/usr/bin/env python3
"""Lightweight redaction helper for context handoff drafts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = [
    (re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[^'\"\s]+"), r"\1=[REDACTED]"),
    (re.compile(r"ghp_[A-Za-z0-9_]{20,}"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"sk-[A-Za-z0-9_-]{20,}"), "[REDACTED_API_KEY]"),
]


def redact(text: str) -> str:
    for pattern, replacement in PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Redact obvious secrets from a Markdown file.")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("--output", help="Output path. Defaults to '<input>.redacted.md'.")
    args = parser.parse_args()

    source = Path(args.input)
    output = Path(args.output) if args.output else source.with_suffix(source.suffix + ".redacted.md")
    output.write_text(redact(source.read_text(encoding="utf-8")), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

