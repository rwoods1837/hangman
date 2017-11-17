#
#Ryan Woods
#
#11/9/17 - 
#
#Hangman Game
#

import random

word = ["trains", "chasecanrun", "krispykreme", "dogs", "cats", "computer", "phone", "iphone", "memes", "olivegarden", "stephensucks", "python"]


def start_screen():
    print ("""
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 

    """)    
                                                                     

def get_puzzle(word):
    return random.choice(word)
    
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
    print("""
******************************************************
*This awesome game was created by Ryan W. on 11/14/17*
******************************************************
    """)
            
def play():
    limit = 10
    strikes = 0
    
    puzzle = get_puzzle(word)
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
