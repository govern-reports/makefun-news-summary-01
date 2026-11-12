"""news-summary-01 entry (Python 3.13, standard library only).

Writes one summary of the world's news of Wednesday 11 November 2026,
in English, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader). The summary is a constant in this file: no network,
no clock, no randomness, so every run writes byte-identical output.
"""

import os
from pathlib import Path

SUMMARY = """World news, Wednesday 11 November 2026:

1. Two days of US-mediated Russia-Ukraine talks in Abu Dhabi ended with agreement on a large prisoner-of-war exchange -- envoy Jared Kushner called it the biggest release of the war -- but no ceasefire and no deal on territory (Reuters). NATO jets were scrambled after drones strayed into Baltic airspace.

2. The COP31 leaders' summit opened in Antalya, Turkey, with 102 heads of state expected over two days; UN Secretary-General Antonio Guterres warned that the slow response to climate change had put the world "on a path to destruction" (AFP/UNFCCC).

3. DR Congo's Ebola outbreak passed 11,000 cases -- 11,042 infections and 5,387 deaths in government figures reported Wednesday -- the country's deadliest outbreak, caused by a Bundibugyo strain with no approved vaccine (AP/Reuters).

4. The US House voted 211-204 to send eight articles of impeachment against Defense Secretary Pete Hegseth to the Judiciary Committee, shelving the bid for this Congress (NPR/Al Jazeera).

5. The US Justice Department charged three Iran-backed operatives over alleged plots in the US and Europe, including a September plot at RAF Fairford in England; Treasury Secretary Scott Bessent moved to a military base after threats (BBC/NYT).

6. British counterterrorism police arrested a 41-year-old US Army soldier in England on suspicion of spying for Russia (BBC).

7. US stocks rose on Wednesday after Tuesday's hotter-than-expected October inflation data -- consumer prices up 0.4%, core up 0.3% -- with a December Federal Reserve rate rise now fully priced; Chicago Fed chief Austan Goolsbee called the report "borderline disturbing" (CNBC/Stocktwits).

8. Bulgaria held a national day of mourning for the 12 people killed in Tuesday's fog pile-ups involving 86 vehicles on the Trakia motorway (BBC).

9. Israeli strikes killed at least eight people in Gaza, Palestinian officials said, as truces in Gaza and Lebanon frayed (Democracy Now)."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    main()
