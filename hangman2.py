#
#Ryan Woods
#
#11/9/17 - 11/20/17
#
#Hangman Game
#
import os
import random
import time

path = "data"
art = "art"

def start_screen():
    with open('art/splash.txt', 'r') as f:
        content = f.read()
    print(content)

def get_puzzle():
    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        with open(path + '/' + f, 'r') as f:
            beginning_lines = f.read().splitlines()
        category_name = beginning_lines[0]
        print(str(i + 1) + ".) " + category_name)

    choice = input("Pick an item " + name + ": ")
    choice = int(choice)
    choice = choice - 1

    file = path + "/" + file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    print(category_name)

    return puzzle

def get_solved(puzzle, guesses):
    solved = ""
    for letter in puzzle:
        if letter in guesses:
            solved += letter

        
        else:
            solved += "-"

    return solved

def get_guess(name):
    while True:
        guess = input("Guess a letter " + name + ": ")
        if guess.isalpha() == True and len(guess) == 1:
            return guess.lower()
        else:
            print("Please input JUST ONE letter")

def display_board(solved, strikes, limit):
    print(solved + "     Strikes: " + str(strikes) + "/" + str(limit))

def win():
    print("Good job " + name + ", You won!!!")

def lose():
    print("Dear " + name + ", YOUR SUCH A LOSER!!! HAHAHAHAHAHAHAHAHAHAHAHA")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n'.")

def credit():
    with open('art/credits.txt', 'r') as f:
        finito = f.read()
    print(finito)
    
    time.sleep(5)
            
def play():
    limit = 10
    strikes = 0
    
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, strikes, limit)

    while solved != puzzle and strikes < limit:
        letter = get_guess(name)

        if letter not in puzzle:
            strikes += 1
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, strikes, limit)

    if solved == puzzle:
        win()
    elif strikes == limit:
        lose()

playing = True
name = input("Whats be thoust name? ")
start_screen()
while playing:
    play()
    playing = play_again()
    
credit()
