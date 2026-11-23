"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. The sealed gate requires UTF-8 text of 1 to 30
characters, not only white space. "kripsang-sekawan" is 16 characters,
so it is written with no trailing newline and no extra bytes.
"""

import os
from pathlib import Path

USERNAME = "kripsang-sekawan"


def _validate(username: str) -> None:
    # Enforce the sealed gate locally: 1-30 chars, one word, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(username) <= 30:
        raise ValueError(f"username must be 1-30 chars, got {len(username)}")
    if username.split() != [username] or not username.strip():
        raise ValueError("username must be a single non-blank word")


def main() -> None:
    _validate(USERNAME)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(USERNAME.encode("utf-8"))


if __name__ == "__main__":
    main()
