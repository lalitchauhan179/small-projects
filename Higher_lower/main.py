from art import logo, vs
from game_data import data
import random


def formated_data(account):
    """formate the account data into  printable format"""
    account_name = account["name"]
    account_discr = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_discr} from {account_country}"


# check if user is correct
## get follower count of each account
## use if statement to chck if user is correct
def check_ans(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
your_score = 0
play_mode = True
account_b = random.choice(data)
# generate a random account from the data
while play_mode:


    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compair A: {formated_data(account_a)}")
    print(vs)
    print(f"Against B: {formated_data(account_b)}")



    # ask user for a guess
    guess = input(" Who Has MOre Followers 'A' or 'B' :  ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_ans(guess, a_follower_count, b_follower_count)


    #give user feedback of their geuss
    if is_correct:
        your_score += 1
        print(f"You're right! Current score: {your_score}")

    else:

        print(f"Sorry, that's wrong. Final score: {your_score}")
        play_mode = False

# give score