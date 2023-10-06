"""
bulls&cows.py: druhý projekt do Engeto Online Python Akademie
author: Katerina Bartuskova
email: kati.bartuskova@gmail.com
discord: bartuskovak
"""

from random import randint

line = ("-"*50)

def has_unique_digits(number) -> bool:
    for element in number:
        if number.count(element) > 1:
            return False
    return True

def choose_number() -> str:
    """
    Choose random four digit number
    between 1023 and 9876 and check,
    if no digit occurs twice in a number.
    """

    number = str(randint(1023,9876))
    if not has_unique_digits(number):
        return choose_number()
    return number

def number_check() -> str:
    """
    Let user enter a number and check,
    if it is four digit, every digit is 
    here only once, and it does not start
    with 0,
    """
    
    number_ok = False
    while not number_ok:
        your_number = input("Enter a number:")
        if your_number == "exit":
            exit(1)
        if not your_number.isnumeric():
            print("You can only use numbers.")
            continue        
        elif not has_unique_digits(your_number):
            print("Use every digit only once")
            continue
        elif len(your_number) != 4:
            print ("Enter a four digit number.")
            continue
        elif your_number[0] == "0":
            print ("Number cannot start with 0.")
            continue
        
        number_ok = True
    
    return your_number

def bull_counter(secret_number: str, number_guess: str) -> int:
    """
    Count bulls (one bull for every correctly
    guessed digit).
    """

    position = 0
    bulls = [0,0,0,0]
    for element in secret_number:
        if element == number_guess[position]:
            bulls[position] = 1
        position += 1
    return bulls
    
def cow_counter(secret_number: str, number_guess, bulls: str) -> int:
    """
    Count cows (one cow for every correct digit,
    but in a wrong place).
    """

    position = 0
    cows = 0
    for element in secret_number:
        if element in number_guess and bulls[position] == 0:
            cows += 1
        position += 1 
    return cows

def game(secret_number: str, number_guess: str) -> str:
    """
    Tells what is your score.
    """

    attempts = 0
    while secret_number != number_guess:
        attempts += 1
        
        bulls = bull_counter(secret_number, number_guess)
        bulls_cnt = bulls.count(1)
        cows = cow_counter(secret_number, number_guess, bulls)

        print(line)
        bullsText = ""
        if bulls_cnt == 1:
            bulls_text = "1 bull"
        elif bulls_cnt != 1 and bulls_cnt != 4:
            bulls_text = str(bulls_cnt) + " bulls" 
        cows_text = ""
        if cows == 1:
            cows_text = "1 cow"
        else:
            cows_text = str(cows) +" cows"
        print(f"{bulls_text}, {cows_text}")

        number_guess = number_check()
    print("Correct, you've guessed right number in", attempts, "guesses!")

if __name__ == "__main__":
    print("Hi there!")
    print(line)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(line)

    secret_number = choose_number()
    number_guess = number_check()
    game(secret_number, number_guess)



