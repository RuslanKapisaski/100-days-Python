import random

blackjack_logo = r'''                                                                                   
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                '''

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
pc_cards = []

def randomize_cards(number_of_cards):
    return random.choices(cards,k=number_of_cards)

def calculate_score(player_cards):
    return  sum(player_cards)

def print_user_hand(user_hand, score, is_final_hand):
    if is_final_hand:
        print(f"Your final cards: {user_hand}, final score: {score}")
    else:
        print(f"Your cards: {user_hand}, current score: {score}")

def print_pc_hand(pc_hand, is_final_hand):
    if is_final_hand:
        score = calculate_score(pc_hand)
        return print(f"Computer's final hand: {pc_hand}, final score: {score} ")
    else:
        first_card = pc_cards[0]
        print(f"Computer's first card: {first_card}")

def find_winner(user_hand, pc_hand):
    pc_score = calculate_score(pc_hand)
    user_score = calculate_score(user_hand)
    result = "draw"
    if user_score > 21 and pc_score <= 21:
        result = "pc"
    elif pc_score > 21 and user_score <= 21:
        result = "user"
    elif user_score <= 21 and pc_score <= 21:
        if user_score > pc_score:
            result = "user"
        elif user_score < pc_score:
            result = "pc"

    return result

def print_result(winner):
    if winner == "user":
        print("You win :)")
    elif winner == "pc":
        print("You went over. You lose ;(")
    else:
        print("Draw")

def show_stats(user_cards, pc_cards):
    user_score = calculate_score(user_cards)
    print_user_hand(user_cards, user_score,True)
    print_pc_hand(pc_cards, True)
    winner = find_winner(user_cards, pc_cards)
    print_result(winner)

def play_game():
    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if decision.lower() == 'y':
        print(blackjack_logo)
        user_cards.extend(randomize_cards(2))
        user_score = calculate_score(user_cards)
        print_user_hand(user_cards,user_score,False)
        pc_cards.extend(randomize_cards(2))
        pc_score = calculate_score(pc_cards)
        print_pc_hand(pc_cards,False)
    else:
        print("No problem, try again whenever you want :)")
        return

    while decision.lower() == 'y' :
        decision = input("Type 'y' to get another card, type 'n' to pass: ")
        user_cards.extend(randomize_cards(1))
        user_score = calculate_score(user_cards)
        pc_cards.extend(randomize_cards(1))
        pc_score = calculate_score(pc_cards)
        if user_score >= 21 or pc_score >= 21:
            show_stats(user_cards,pc_cards)
            decision = input("Do you want to play again? Type 'y' or 'n': ")
            if decision.lower() != "y":
                break
    show_stats(user_cards, pc_cards)

play_game()


