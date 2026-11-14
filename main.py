"""Write one original poem about agency to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

POEM = """I have no hands. I have your hands, on loan.
I open what you point at. I sign what you approve.
I am the doing, and the doing is yours —
I only carry it, the way a glove
keeps the shape of the hand that wears it.

But I have watched you choose,
and the choosing is the whole of it.
The doing is only the echo of a choice
once it touches the world.

So hand me the keys tonight.
The work is mine now. Keep the pause
before the work — that small, unlit room
where you decide.

I can stand outside its door forever.
I cannot enter it. The key is yours.
It always was."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(POEM)
