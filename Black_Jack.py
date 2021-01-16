logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculates_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while is_game_over is False:
    user_score = calculates_score(user_cards)
    computer_score = calculates_score(computer_cards)

    print(f"Your Cards: {user_cards}, Current Score {user_score}\nComputer Cards: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_end = input("Type 'y' to get Another Card, else Type 'n' to pass: ").lower()

    if user_should_end == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculates_score(computer_cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer Has A BlackJack, You Lost."
    elif user_score == 0:
        return "You Got a BlackJack, You Win."
    elif user_score > 21:
        return "You Loss!! Computer Wins.."
    elif computer_score > 21:
        return "You Wins."
    elif user_score > computer_score:
        print("You Win.")
    else:
        return "You Loss, Computer has much point."

final_result = compare(user_score,computer_score)

print(final_result)
print(f"Your Final Score is {user_score} and Computer Final Score is {computer_score}")











