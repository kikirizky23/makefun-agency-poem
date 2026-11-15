# The Relief — agency-poem-01 v5

A lighthouse keeper hands the lamp to his successor.

## What v5 fixes vs v4

v4's `main.py` only printed the poem to stdout and never wrote
`/output/entry.txt`, so the server's dev grade failed the
"Wrote /output/entry.txt" check (0/1, valid 0, not prize-eligible).

v5 keeps the exact same poem ("The Relief", 755 characters) and
restores the file-writing logic from v3:

- writes the poem verbatim as UTF-8 to `/output/entry.txt`
- reads the file back and verifies its bytes equal the poem exactly
  (byte-level comparison, exits 1 on any mismatch)
- validates the poem length is within 1–1000 characters
- also prints the poem to stdout

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` and prints the poem. Exit 0 on success.
