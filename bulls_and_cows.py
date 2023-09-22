"""
bulls&cows.py: druhý projekt do Engeto Online Python Akademie
author: Katerina Bartuskova
email: kati.bartuskova@gmail.com
discord: bartuskovak
"""

from random import randint
import math

def choose_number():
     number = "1234" #str(randint(1023,9876))
     for element in number:
         if number.count(element) > 1:
           return choose_number()
     return number

def number_check():
    your_number = input("Enter a number:")
    print("-"*50)
    if len(your_number) != 4:
        raise ValueError ("Enter a four digit number.")
    elif your_number[0] == "0":
        raise ValueError ("Number cannot start with 0.")
    elif your_number.isnumeric():
        print(">>>", your_number)
    else:
        raise ValueError ("You can only use numbers.")
    return your_number
    
def cow_counter(secret_number, number_guess, bulls):
    position = 0
    cnt = 0
    for element in secret_number:
        if element in number_guess and bulls[position] == 0:
            cnt += 1
        position += 1 
    return cnt
    

def bull_counter(secret_number, number_guess):
    position = 0
    bulls = [0,0,0,0]
    for element in secret_number:
        if element == number_guess[position]:
            bulls[position] = 1
        position += 1
    return bulls
      
    

def game(secret_number, number_guess):
    attempts = 0
    while secret_number != number_guess:
        attempts += 1
        
        bulls = bull_counter(secret_number, number_guess)
        bullsCnt = bulls.count(1)
        cows = cow_counter(secret_number, number_guess, bulls)

        print("-"*50)
        bullsText = ""
        if bullsCnt == 1:
            bullsText = "1 bull"
        elif bullsCnt != 1 and bullsCnt != 4:
            bullsText = str(bullsCnt) + " bulls" 
        cowsText = ""
        if cows == 1:
            cowsText = "1 cow"
        else:
            cowsText = str(cows) +" cows"
        print(f"{bullsText}, {cowsText}")

        number_guess = number_check()
    print("Correct, you've guessed right number in", attempts, "guesses!")



############################################
if __name__ == "__main__":
    print("Hi there!")
    print("-"*50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-"*50)

    secret_number = choose_number()
    number_guess = number_check()
    game(secret_number, number_guess)



