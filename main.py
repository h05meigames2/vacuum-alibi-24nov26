"""The Vacuum's Alibi — one line, max 200 characters.

Writes the funniest one-line excuse a robot vacuum can give for
missing a spot, in flat deadpan robot voice, to entry.txt.
"""

import hashlib
import os

LINE = (
    "That spot was not missed. Per Section 4 of my cleaning mandate, "
    "it has been reclassified as a protected dust habitat."
)


def validate(line: str) -> None:
    """Enforce the competition rules: 1-200 chars, single line, non-blank."""
    assert isinstance(line, str), "line must be a string"
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert line, "line must not be empty"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    digest = hashlib.sha256((LINE + "\n").encode("utf-8")).hexdigest()
    print(f"Wrote {path} ({len(LINE)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
