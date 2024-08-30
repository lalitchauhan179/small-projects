from random import randint
from art import logo
EASY_MODE = 10
HARD_MODE = 5


def play_game():
    print(logo)
    print("Welcome to The number Guessing Game! ")
    print("I'm Thinking of a number between 1 and 100 ! ")
    random_number = randint(2, 100)
    # print(f"the random number is {random_number}")

    def easy_mode():
        global EASY_MODE
        while EASY_MODE != 0:
            print(f"you have {EASY_MODE} attempts remaining chances left")
            guess = int(input("make a gess:  "))
            if guess != random_number:
                EASY_MODE -= 1
                if guess > random_number:
                    print("too High ")
                elif guess < random_number:
                    print("too LOw ")
                easy_mode()
            else:
                print(f"you got the ans right! {random_number}")

    def hard_mode():
        global HARD_MODE
        while HARD_MODE != 0:
            print(f"you have {HARD_MODE} attempts remaining chances left")
            guess = int(input("make a gess:  "))
            if guess != random_number:
                HARD_MODE -= 1
                if guess > random_number:
                    print("too High ")
                elif guess < random_number:
                    print("too LOw ")
                hard_mode()
            else:
                print(f"you got the ans right! {random_number} ")

    difficulty = input("choose a difficulty 'easy ' of 'hard':  ").lower()
    if difficulty == "easy":
        easy_mode()
    elif difficulty == "hard":
        hard_mode()


try_agin = input("would you like to play a game of gess the number 'y' 'n' ")
if try_agin == "y":
    play_game()
