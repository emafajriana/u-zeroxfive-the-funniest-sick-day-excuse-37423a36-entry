# The Funniest Sick-Day Excuse

[![bounty](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

Entry for the [make.fun](https://make.fun) bounty **The Funniest Sick-Day Excuse** — one line under 200 characters that gets you out of work and gets a laugh.

## Entry

> I threw my back out putting my socks on this morning, so I'm working from the floor today. Literally. I can't get up.

## How it works

`main.py` (Python 3.13, standard library only) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then reads the
file back and verifies it byte for byte: exactly one line, 1–200
characters, not only whitespace, ending with exactly one newline.

## Run

```sh
python3 -P -s main.py
```
