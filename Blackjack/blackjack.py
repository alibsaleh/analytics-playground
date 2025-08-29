import random
import art
# from itertools import filterfalse  # (unused)

## first hand outcome
def first_hand(game_deck):
    player = []
    dealer = []
    x = 2
    while x > 0:
        card_drawn = random.choice(game_deck)
        game_deck.remove(card_drawn)
        player.append(card_drawn)

        card_drawn = random.choice(game_deck)
        game_deck.remove(card_drawn)
        dealer.append(card_drawn)
        x -= 1

    return player, dealer, game_deck

# show the results after first hand
def result(player_cards, dealer_cards):
    player_score = sum(player_cards)

    if sum(player_cards) == 21 and sum(dealer_cards) < 21:
        print(f"Your cards: {player_cards}")
        print(f"Dealer's cards: {dealer_cards}")
        print("You win with Black Jack! 😄")
        return  # FIX: stop here

    elif sum(player_cards) < 21 and sum(dealer_cards) == 21:
        print(f"Your cards: {player_cards}")
        print(f"Dealer's cards: {dealer_cards}")
        print("You lose! Dealer wins with Black Jack! 😥")
        return  # FIX

    elif sum(player_cards) == 21 and sum(dealer_cards) == 21:
        print(f"Your cards: {player_cards}")
        print(f"Dealer's cards: {dealer_cards}")
        print("Draw! You both have Black Jack! 😤")
        return  # FIX

    else:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's cards: {dealer_cards[0]}")

############# GAME CONTINUE FUNCTIONS

# player chooses no more cards
def no_more_cards(player, dealer, game_deck):
    player_score = sum(player)
    dealer_score = sum(dealer)

    # Early outcomes when dealer already at/above 17
    if player_score == dealer_score and player_score >= 17:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print(f"Draw! You both have {player_score}! 😤")
        return  # FIX

    if dealer_score >= 17 and dealer_score > player_score:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print(f"You lose! 😥")
        return  # FIX

    if dealer_score >= 17 and dealer_score < player_score:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print(f"You Win! 😄")
        return  # FIX

    # Dealer draws up to 17+
    while dealer_score < 17:
        if not game_deck:  # FIX: guard to avoid empty-deck error
            raise RuntimeError("Deck empty before dealer draw")

        card_drawn = random.choice(game_deck)
        game_deck.remove(card_drawn)
        dealer.append(card_drawn)

        # FIX: recompute & adjust Aces every draw
        dealer_score = sum(dealer)
        aces = dealer.count(11)
        while dealer_score > 21 and aces:
            dealer_score -= 10
            aces -= 1

    # After dealer finished drawing (dealer_score >= 17)
    if dealer_score > 21:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print("You Win! 😄")
        return

    if dealer_score > player_score:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print("You lose! 😥")
        return

    if dealer_score == player_score:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print(f"Draw! You both have {player_score}! 😤")
        return

    # Otherwise player_score > dealer_score
    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
    print("You Win! 😄")
    return

def more_cards(player, dealer, game_deck):
    dealer_score = sum(dealer)
    player_score = sum(player)

    ## player draws while under 21
    while player_score < 21:
        if not game_deck:  # FIX: guard
            raise RuntimeError("Deck empty before player draw")

        card_drawn = random.choice(game_deck)
        game_deck.remove(card_drawn)
        player.append(card_drawn)

        # FIX: recompute & adjust Aces for player
        player_score = sum(player)
        aces = player.count(11)
        while player_score > 21 and aces:
            player_score -= 10
            aces -= 1

        if player_score >= 21:
            break  # stop drawing on 21 or bust

        another_card = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
        if another_card != 'y':
            break

    #### resolve outcomes or let dealer draw
    if player_score > 21:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print("You lose! 😥")
        return

    if dealer_score >= 17:
        if player_score > dealer_score:
            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
            print("You Win! 😄")
            return
        elif player_score == dealer_score:  # FIX: handle draw
            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
            print(f"Draw! You both have {player_score}! 😤")
            return
        else:
            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
            print("You lose! 😥")
            return

    # Dealer draws up to 17+
    while dealer_score < 17:
        if not game_deck:  # FIX: guard
            raise RuntimeError("Deck empty before dealer draw")

        card_drawn = random.choice(game_deck)
        game_deck.remove(card_drawn)
        dealer.append(card_drawn)

        # FIX: recompute & adjust Aces every draw
        dealer_score = sum(dealer)
        aces = dealer.count(11)
        while dealer_score > 21 and aces:
            dealer_score -= 10
            aces -= 1

    # Final compare
    if dealer_score > 21:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print("You Win! 😄")
        return
    if dealer_score > player_score:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print("You lose! 😥")
        return
    if dealer_score == player_score:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
        print(f"Draw! You both have {player_score}! 😤")
        return

    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Dealer's cards: {dealer}, current score: {dealer_score}")
    print("You Win! 😄")
    return

# ========= Game loop =========
game_on = True
while game_on:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    game_decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if game_decision != 'y':
        break

    print(art.logo)

    number_of_decks = int(input("How many decks do you want to play with? "))
    game_cards = number_of_decks * cards  # e.g., 4 decks → 52 value-cards

    # first deal
    player_cards, dealer_cards, game_cards = first_hand(game_cards)
    result(player_cards, dealer_cards)

    # If either side has blackjack, go to next round
    if sum(player_cards) == 21 or sum(dealer_cards) == 21:
        continue

    # Player decision
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
    if another_card == 'n':
        no_more_cards(player_cards, dealer_cards, game_cards)
    else:
        more_cards(player_cards, dealer_cards, game_cards)