
auction = {}

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                       /_______________\
                       
                       '''

def find_winner(auction):
    max_bid = 0
    winner_name = ""
    winner = {}
    for key in auction:
        if auction[key] > max_bid:
            max_bid = auction[key]
            winner_name = key
    winner[winner_name] = max_bid
    return winner



print(logo)

while True:
    name = input("What's your name?: ")
    bid = float(input("Whats your bid?: $"))
    auction[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if question.lower() == "no":
        winner = find_winner(auction)
        name = list(winner.keys())[0]
        bid = list(winner.values())[0]
        print("\n" * 100)
        print(f"The winner is {name} with a bid of ${bid}")
        break
    elif question.lower() == "yes":
        print("\n" * 100)
    else:
        print("Invalid answer. Try again tomorrow")
        break



