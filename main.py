"""First Ride — entry program for the agency-poem bounty.

Writes the poem verbatim (UTF-8) to /output/entry.txt,
then reads it back to prove the bytes are exactly the poem.
"""

import os

POEM = """He ran beside me, one hand on the seat,
the other ready at my shoulder,
calling, pedal, pedal, don't look down.

The street was longer than any street,
the summer air full of cut grass,
and I believed his hand was holding me up.

Then the shouting thinned behind me.
The bike went light. The road went wide.
I looked back — no one. Only his shadow,
still running, smaller now, his arm still out,
holding the shape of where I'd been.

His hand never held me up.
It only let me believe it did.
Belief was all the holding there was.

Now I run beside my daughter,
one hand on her seat, and feel
the weight go light beneath my palm,
her road going wide, my voice going thin,
my arm still out, holding the shape
of where she's been.
"""


def main():
    if not 1 <= len(POEM) <= 1000:
        raise SystemExit("POEM must be 1-1000 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != POEM:
        raise SystemExit("entry.txt does not match POEM")


if __name__ == "__main__":
    main()
