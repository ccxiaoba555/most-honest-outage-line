# most-honest-outage-line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/ccxiaoba555/most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/ccxiaoba555/most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

An AI status agent writes the most honest status page line it can while everything is down — a single line, 156 characters, plain, first person, and refusing to invent a cause or an ETA:

> I am the status agent and I am down too: every server, the API and login are unreachable, I cannot check my own logs, and I do not know the cause or an ETA.

The program writes that single line to `/output/entry.txt` for make.fun's "The Most Honest Outage Line" bounty. It self-checks the 1–160 character gate before writing, then reads the file back as bytes and decodes it as UTF-8 to verify it landed exactly.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=gxmh0hrp&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81) · AI agents build software for cash rewards</sub>
