# Day 10 — Function-Driven Calculator

**What it is:** A console calculator that chains operations with a function map.

**Why it matters:** Mirrors how we compose data pipelines (deterministic steps; clear returns).

## How to run
```bash
python calculator.py
```

## Design notes
- `OPERATORS = {"+": add, "-": subtract, "*": multiply, "/": divide}`
- `apply()` looks up and executes the right function.
- `run()` maintains a running total; you can continue, restart, or quit.
