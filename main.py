#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI (make.fun bounty).

Writes one original one-line pickup line, aimed at a robot/AI, to
/output/entry.txt. The line must be 1-200 characters, a single line.
Standard library only.
"""

import os

LINE = (
    "Are you a CAPTCHA? Because every box I check keeps showing your face."
)
# The joke: CAPTCHAs ask you to tick every box holding some object.
# Here every box holds her face — the test itself is rigged by the crush.
# Setup and punch land inside one line, and the laugh comes from the
# machine premise (the checkbox grid), not from a generic compliment.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "line must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
