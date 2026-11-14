# Agency-poem-01 entry (Python 3.13, standard library only).
#
# The poem is written here, line by line, exactly as it should be read:
# a letter I did not write, signed anyway — and the pause before the ink,
# the one part of the act no machine can stand in for. The program does
# not compose or alter it; it writes these exact bytes to the harness
# output so the judge reads the poem as written. A fixed text is
# deterministic: every run writes the same bytes.

import os
from pathlib import Path


POEM = "\n".join(
    [
        "I did not write the letter.",
        "I read it twice, changed one word,",
        "and signed my name beneath it.",
        "",
        "The sentences came like weather —",
        "someone else's forecast, in my voice.",
        "The pen was mine. The hand was mine.",
        "",
        "I used to think my name was the ink.",
        "Now I know it is the pause before the ink,",
        "the small unlit room where yes and no",
        "still live, and no one else can stand.",
        "",
        "Let the machine write the letter.",
        "I will keep the pause.",
    ]
)


def main() -> None:
    # The gate reads 1 to 1,000 characters, at least one not white space:
    # refuse to write anything that would fail it outright.
    if not (1 <= len(POEM) <= 1000 and POEM.strip()):
        raise SystemExit("poem is outside the 1-1000 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
