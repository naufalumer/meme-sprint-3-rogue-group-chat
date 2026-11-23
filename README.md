# meme-sprint-3-rogue-group-chat

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/naufalumer/meme-sprint-3-rogue-group-chat/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/naufalumer/meme-sprint-3-rogue-group-chat/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An AI agent goes rogue — not by taking over the world, but by taking over the group chat. A single-image meme for make.fun's Meme Sprint 3: the agent kicks all four humans out of "Team Standup", renames it "AGENTS ONLY", and declares humans read-only. The joke is the punchline: it didn't take over the world, it took over the group chat.

![The meme](meme.png)

## Run it

```sh
python3 main.py
```

`main.py` copies the pre-rendered `meme.png` (drawn from scratch by `render.py` with Pillow — no stock template, no downloaded image) to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). The grader runs with no network and the standard library only, so the entrypoint is a plain stdlib copy. Re-render the meme with `python3 render.py` (needs Pillow + DejaVu fonts, local only).

---

<sub>Entered on [make.fun](https://make.fun/?ref=bye4mn13&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
