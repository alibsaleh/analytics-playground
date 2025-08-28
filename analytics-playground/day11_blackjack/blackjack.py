# Day 11 — Blackjack (stub)
# Structure only — implement the logic yourself (no spoilers).

def deal(deck):
    raise NotImplementedError("Implement me")

def hand_score(hand):
    # TODO: handle Aces (11 → 1) when total > 21
    raise NotImplementedError("Implement me")

def player_turn(hand, deck):
    # TODO: loop input: 'h' to hit, 's' to stand
    raise NotImplementedError("Implement me")

def dealer_turn(hand, deck):
    # TODO: dealer hits until 17+
    raise NotImplementedError("Implement me")

def compare(player_score, dealer_score):
    # TODO: return 'win'/'lose'/'push'
    raise NotImplementedError("Implement me")

def main():
    print("Blackjack — implement the game flow here.")

if __name__ == "__main__":
    main()
