"""First Ride — entry program for the agency-poem bounty.

Writes the poem verbatim (UTF-8) to /output/entry.txt.
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

I didn't fall. I kept going.
And somewhere behind me, his hand
closed on nothing, and stayed open.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
