print("Welcome to the secret auction program.")

auction = True
auction_bids = {}

while auction:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_bids[name] = bid

    other_bidders = input("Are there other bidders? Type 'yes' or 'no': ").strip().lower()
    if other_bidders == 'yes':
        continue
    else:
        auction = False

# Determine winner
highest_bid = 0
winning_name = ''
for bidder in auction_bids:
    if auction_bids[bidder] > highest_bid:
        highest_bid = auction_bids[bidder]
        winning_name = bidder

print(f"The winner is {winning_name} with a bid of ${highest_bid}.")
