#!/usr/bin/env python3
"""The Relief — agency-poem-01 v4 entry.

A lighthouse keeper hands the lamp to his successor.
Prints the poem to stdout.
"""

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

print(POEM)
