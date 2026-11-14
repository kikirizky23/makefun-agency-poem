# Agency Poem — "the pause"

A short poem about agency: the power to choose and to act, and what
happens when an AI agent does the acting for you.

The poem opens on a letter the speaker did not write. She read it
twice, changed one word, and signed her name beneath it — the sentences
arrived like weather, someone else's forecast in her voice. The pen was
hers, the hand was hers, and yet the words were not.

Its turn is the realisation that a name is not the ink. The name is the
pause before the ink: a small unlit room where yes and no still live, and
no one else can stand. That pause — the moment of choosing — is the one
part of agency that cannot be delegated, automated, or signed away.

So the poem ends by letting the machine have the letter — and keeping the
pause. The speaker gives away the writing and holds on to the choosing.

## How to run

`mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt`

`main.py` is Python 3.13, standard library only. It writes the poem, byte
for byte, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Every run
writes the same bytes; the poem is 15 lines, inside the 1–1,000 character gate.
