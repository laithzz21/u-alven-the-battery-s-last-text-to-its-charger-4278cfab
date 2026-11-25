# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/laithzz21/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/laithzz21/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the make.fun bounty "The Battery's Last Text to Its Charger": the
phone battery's last text message to the charger it waited for all day, as
one line of plain text of at most 200 characters.

## Entry

> Hey charger, it's me — your battery. I've been clinging to 1% since noon just to say goodbye. Come home soon, I'm fading fast. Love, your phone.

Exact character count: **144** (limit: 200). Single line, plain text.

## How to run

```sh
python3 main.py
```

Prints exactly the entry text to stdout (no trailing newline) and exits 0.
Deterministic — Python 3.12, standard library only, no network, clock, or
randomness. If stdout is unavailable, it falls back to writing the entry to
`$MAKEFUN_OUTPUT` or `./output/entry.txt`.
