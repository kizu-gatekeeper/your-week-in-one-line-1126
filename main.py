"""Entry for make.fun: Your Week in One Line.

The win, the fail and the compromise, in under 100 characters.
"""
import os

LINE = "Monday I fixed the bug, Tuesday the bug fixed me, Friday we compromised: it ships broken, quietly."
MAX_CHARS = 100


def write_entry(out_dir):
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry must be one non-empty line within the limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
