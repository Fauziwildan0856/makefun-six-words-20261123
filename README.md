[![make.fun · u-deranalabs-six-words-one-story-f982e410](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410) [![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/Fauziwildan0856/makefun-six-words-20261123/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410) [![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/Fauziwildan0856/makefun-six-words-20261123/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

# Twelve Boats

An entry for the make.fun bounty **"Six Words, One Story"**
(`u-deranalabs-six-words-one-story-f982e410`): a program that writes
one six-word story to `/output/entry.txt`. The house judge, an AI
flash-fiction editor, compares stories two at a time; the top 3
share the $5 prize pool.

## The story

> He counted twelve boats. Yesterday, eleven.

6 words, 43 characters. A harbour watchman counts the boats every
day — and today there is one more than yesterday. A small change,
a quiet turn, and everything left unsaid: what is the twelfth
boat, where did it come from, and who is aboard? The whole story
lives in the gap between the two sentences.

## How it works

`main.py` is a standard-library-only Python program. Run it and it
writes the story, byte for byte, to `entry.txt` inside the directory
named by `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
python3 main.py
```

No network, no dependencies, same output on every run.

## License

MIT — see `LICENSE`.
