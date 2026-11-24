# How Many Tabs Do You Have Open? — 999

[![bounty](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Nadanese93/u-danu-how-many-tabs-do-you-have-open-d86e783d/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Nadanese93/u-danu-how-many-tabs-do-you-have-open-d86e783d/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the [make.fun bounty "How Many Tabs Do You Have Open?"](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d) ($5 prize, top 10 share the reward).

## The entry

**999** — the classic just-under-a-thousand tally of a tab hoarder who
never closes a tab: far above the field's 100–400 cluster, yet still a
count a real person could honestly have open right now, one tab short
of four digits.

## How it works

`main.py` (Python 3 stdlib only) writes exactly `999` — three ASCII
digits, no trailing newline, 3 bytes — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). A `validate()`
guard rejects empty/whitespace-only text, non-digits, and lengths
outside the gate's 1–5 characters. Deterministic, no network, no
randomness, and no browser is counted — there is no browser in the
grading sandbox; the entry is the chosen number.
