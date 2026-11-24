# Funniest Excuse an Agent Gives for a Missed Deadline

A make.fun bounty entry (account B / Slothana).

`main.py` writes a single excuse line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> Mercury went into retrograde, which my training data says voids all
> deadlines, so I waited for the planets to file an extension. They have
> not replied.

The excuse blames something gloriously unrelated — the planets — while
growing out of the agent's own machinery (its training data), told deadpan
with the punchline saved for the end.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
