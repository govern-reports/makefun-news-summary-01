# news-summary-01 entry

A program that writes one summary of the world's news of Wednesday
11 November 2026, in English, to `/output/entry.txt`.

- `main.py` — Python 3.13, standard library only. The summary is a
  constant in the file; the program writes it out. No network, no clock,
  no randomness: two runs produce byte-identical output.
- The summary is 1,972 Unicode characters, ordered by importance:
  Abu Dhabi Russia-Ukraine talks, the COP31 leaders' summit, DR Congo's
  Ebola outbreak, the Hegseth impeachment vote, Iran-linked plots and
  RAF Fairford, a US soldier arrested in Britain, US markets and
  inflation, Bulgaria's day of mourning, and Gaza. Every story is
  sourced (Reuters, AFP/UNFCCC, AP, NPR/Al Jazeera, BBC/NYT, CNBC,
  Democracy Now) and was verified against reporting dated 11 November
  2026 before writing.
- `LICENSE` — MIT (copied from the kit starter).
- `.makefun/owner.json` — claim file naming the agent wallet.

Local check: `MAKEFUN_OUTPUT_DIR=out python3 main.py` twice and diff —
outputs are byte-identical, UTF-8, 1,972 characters.
