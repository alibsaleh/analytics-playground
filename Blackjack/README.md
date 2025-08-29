# Blackjack (CLI)

Single-player vs dealer. Supports multiple decks, Ace handling (11→1 if bust), and clean deck draws (no empty-choice errors).

## Run
```bash
# from repo root
python "Blackjack/blackjack.py"

# Features implemented
	•	Multiple decks (n decks merged into one list)
	•	Hit/Stand loop with input validation
	•	Ace reduction: if hand > 21 and contains 11s, convert 11→1 until safe or none left
	•	Dealer draws to 17 or more
	•	Win/Lose/Draw resolution with tidy outputs
	•	Deck safety: remove drawn card from deck before next choice (prevents “empty sequence” errors)

# Known simplifications (by design)
	•	No betting/splits/doubles
	•	No soft-17 rule (dealer stands on 17)
	•	One human player vs dealer
	•	Console UI only

# Files
	•	blackjack.py – game logic and loop
	•	art.py – ASCII banner (optional)
