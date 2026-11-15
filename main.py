#!/usr/bin/env python3
"""The Relief — agency-poem-01 v5 entry.

A lighthouse keeper hands the lamp to his successor.
Writes the poem verbatim (UTF-8) to /output/entry.txt,
reads it back to prove the bytes are exactly the poem,
and also prints it to stdout.

v5 fixes v4: v4 only printed the poem and never wrote the file,
so the server's dev grade failed ("Wrote /output/entry.txt" 0/1).
"""

import os
import sys

POEM = """For thirty winters I climbed the iron stairs
with oil on my cuffs and the wind in my teeth,
turned the wick, and sent the light out
to find the ships before the rocks could.

Tonight my hands shook at the top step.
The lamp glass rattled. The boy beside me —
the one I taught to trim a wick —
reached past my shoulder, steadied the flame,
and the light leaned toward his steadier hand.

I did not let go all at once.
I showed him where the glass fogs first,
where the oil thickens in January,
how to listen for the hinge that sticks.

Then I took the stairs down, one slow step at a time,
and stood on the rocks where the ships pass.
Above me the lamp turned, and turned,
and the beam came back across the water,
and found me standing in it, empty-handed."""

length = len(POEM)
if not 1 <= length <= 1000:
    print(f"error: poem length {length} characters is outside the 1-1000 range",
          file=sys.stderr)
    sys.exit(1)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as handle:
    handle.write(POEM)

with open("/output/entry.txt", "rb") as handle:
    written = handle.read()
if written != POEM.encode("utf-8"):
    print("error: /output/entry.txt bytes do not match the poem", file=sys.stderr)
    sys.exit(1)

print(POEM)
