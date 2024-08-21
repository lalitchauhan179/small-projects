from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
def calculator():
    print(logo)
    try_agan = True
    first_num = float(input("type the first number:-  "))
    while try_agan:
        for symbol in operations:
            print(symbol)
        operator = input(f"type a mathematical operator a choice :-  ")
        second_num = float(input("type the second number:-  "))

        result = operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} :- {result}")

        user_chioce = input(f"do you want to continue with {result} type 'y' or do you want new calculator press 'n' :- ").lower()
        if user_chioce == "y":
            first_num = result
        elif user_chioce == "n":
            try_agan = False
            print("\n" * 20)
            calculator()

calculator()






