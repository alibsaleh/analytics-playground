# Analytics Playground

Small, focused Python projects that harden the *engineering habits* behind modern analytics & AI systems.  
This repo is part of my ongoing skills sprint to improve automation, reliability, and decision support in my day-to-day work.

> **Note:** All examples use synthetic data. Views are my own.

---

## Why this matters (for real work)

- **Deterministic logic over vibe-coding.** Clear inputs/outputs and pure functions make code testable and chainable.
- **LLM/Agent tie-ins.** Function routing, state handling, and validation here mirror the building blocks of analytics copilots.
- **Operations mindset.** Small, correct utilities roll up into dependable pipelines, dashboards, and decision support.

---

## Projects

| Project | What it does | Why it matters (analytics/AI) |
|---|---|---|
| **Secret Auction** (`Secret Auction/`) | CLI app to collect bids, store in a dictionary, compute the winner. | Mirrors **event capture → aggregation → decision**. Dicts/JSON maps are how services & agents pass state. |
| **Function-Driven Calculator** (`Calculator/`) | Calculator that chains operations using a **function map** (`{'+': add, ...}`) and returns values for reuse. | Same pattern as **agent tool routing**: map an intent/symbol to a callable. Demonstrates pure functions, reusability, and state hand-off. |
| **Blackjack** ('Blackjack/') | Game loop, deck state, decisions, scoring. | Encodes **rules & edge cases**—excellent practice for guardrails, validation, and flow control used in data/LLM pipelines. |

---

## Skills demonstrated

- Functions & **returns vs prints** • control flow • input validation  
- **Function maps / dispatch** • dictionaries & basic data structures  
- Modularization & readability (comments/docstrings)  
- Edge-case thinking (invalid input, divide-by-zero, ties, etc.)

**AI/LLM parallels**

- Function map → **tool/skill routing** in agents  
- Clean returns → **chainable steps** in pipelines and prompts  
- Input checks → **guardrails & prompt hygiene**  
- Minimal state → easier **testing & reproducibility**

---

## Run locally

```bash
# From repo root
python "Secret Auction/main.py"
python "Calculator/calculator.py"   # or main.py if you prefer
