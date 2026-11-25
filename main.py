#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes one status page line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). The line is written in the first person by the AI
status agent itself, during a total outage:

- it names what is down (every server, the API and login),
- it admits the agent is down too and cannot check its own logs —
  the one tool it would normally trust to explain an outage,
- it refuses to invent a cause or an ETA, because a guessed restore
  time on a status page is just a second, slower outage of trust.

Gate (from competition.yaml): entry.txt must be UTF-8 text of 1 to 160
characters, not only whitespace. This program self-checks that cap before
writing and reads the file back to verify it landed exactly.
"""

import os
import sys

MAX_CHARS = 160

LINE = (
    "I am the status agent and I am down too: every server, the API and "
    "login are unreachable, I cannot check my own logs, and I do not know "
    "the cause or an ETA."
)


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: line is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)

    with open(out_path, "rb") as fh:
        raw = fh.read()
    back = raw.decode("utf-8")  # gate requires valid UTF-8; raises if not
    if back != text or not (1 <= len(back) <= MAX_CHARS) or not back.strip():
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(back)} chars)")
    print(back)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
