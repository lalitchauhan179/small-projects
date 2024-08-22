from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "its a draw ! what is this luck 😫😫"
    elif computer_score == 0:
        return "you loose ! computer got blackjack 🃏🃏🃏"
    elif user_score == 0:
        return "you wan with blackjack 🃏🃏🃏"
    elif user_score > 21:
        return "you went over you loose 😛😛😛"
    elif computer_score > 21:
        return "computer went over you won 🤔🤔🤔"
    elif computer_score > user_score:
        return "You loose 😑😑😑😑"
    elif user_score > computer_score:
        return "you win! 🏆🏆"
    else:
        return "you loose 😛😛😛 "


def play_mode():
    print(logo)
    user_cards = []
    computers_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computers_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computers_cards)
        print(f"Your cards : {user_cards} currunt score : {user_score}")
        print(f"computers first hand : {computers_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("do you want another card 'y' or 'n' to pass")
            if another_card == "y":
                user_cards.append(deal_card())
            elif another_card == "n":
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)
        print(f"users final cards {user_cards} users final score {user_score}")
        print(f"computers  hand : {computers_cards} computer final score : {computer_score}")
        print(compare(user_score, computer_score))


while input(" Would you like to play a game of blackjack 'y' or  'n' ") == "y":
    print("\n" * 100)
    play_mode()


