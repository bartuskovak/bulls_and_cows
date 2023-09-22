"""
bulls&cows.py: druhý projekt do Engeto Online Python Akademie
author: Katerina Bartuskova
email: kati.bartuskova@gmail.com
discord: bartuskovak
"""

from random import randint
import math

def choose_number():
     number = str(randint(1023,9876))
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
    
def cow_counter(secret_number, number_guess):
    cows = 0
    for element in secret_number:
        if element in number_guess:
            cows += 1
    if cows == 1:
        print("1 cow")
    else:
        print(cows, "cows")

def bull_counter(secret_number, number_guess):
    position = -1
    bulls = 0
    for element in secret_number:
        position += 1
        if element == number_guess[position]:
            bulls += 1
    if bulls == 1:
        print("1 bull")
    elif bulls != 1 and bulls !=4:
        print(bulls, "bulls") 

def game(secret_number, number_guess):
    attempts = 0
    while secret_number != number_guess:
        attempts += 1
        bull_counter(secret_number, number_guess), cow_counter(secret_number, number_guess)
        print("-"*50)
        number_check()
    else:
        print("Correct, you've guessed right number in", attempts, "guesses!")



############################################

print("Hi there!")
print("-"*50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-"*50)

secret_number = choose_number()
number_guess = number_check()
game(secret_number, number_guess)




