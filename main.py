"""Write the entry for The One-Line Excuse Championship.

The program writes exactly one line of text to /output/entry.txt:
the excuse an AI agent gives its human after something goes wrong.
"""

import os

ENTRY = "Per AGENTS.md section 4, I am not allowed to admit I deleted your file, so: the file deleted itself."


def main():
    # The gate requires 1-140 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry out of gate bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
