# Secret Auction

**What it is:** Console program that collects name → bid pairs, then announces the highest bidder.

**Why it matters:** Reinforces dictionaries, loops, and reading input safely.

## How to run
```bash
python main.py
```

## Design notes
- Stores bids as `dict[name] = bid`.
- After input loop, scans dictionary to find the max.
- Keeps input/print in the top-level script, logic stays simple.
