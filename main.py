#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single one-line sick-day excuse to <output>/entry.txt.
Stdlib only. Deterministic: the same bytes every run.
"""

import os
from pathlib import Path

ENTRY = (
    "I threw my back out putting my socks on this morning, "
    "so I'm working from the floor today. Literally. I can't get up."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY + "\n", encoding="utf-8")
    # Read-back gate: the written file must hold exactly our entry,
    # byte for byte, with exactly one trailing newline.
    written_bytes = target.read_bytes()
    assert written_bytes == (ENTRY + "\n").encode("utf-8"), \
        "entry.txt content mismatch"
    assert written_bytes.endswith(b"\n") and not written_bytes.endswith(b"\n\n"), \
        "entry.txt must end with exactly one newline"
    assert 1 <= len(ENTRY) <= 200, "entry length out of gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"


if __name__ == "__main__":
    main()
