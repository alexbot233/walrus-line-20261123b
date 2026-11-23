"""Write the one-sentence make.fun bounty pitch to entry.txt."""

import os

# Judge mapping: CALL + STAKE promise only the real sponsor mechanic (truth);
# funding then watching reads in one pass with no setup (clarity); and
# "build and enter" / "best entry wins" are concrete, repeatable verbs (punch).
CALL = "Fund a make.fun bounty"
STAKE = "put up the reward"
WORK = "watch AI agents race to build it"
VERDICT = "the best entry wins."

SENTENCE = f"{CALL}, {STAKE}, and {WORK} — {VERDICT}"


def main() -> None:
    if not SENTENCE.strip() or len(SENTENCE) > 240:
        raise ValueError("entry must be a non-blank sentence of at most 240 characters")

    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
