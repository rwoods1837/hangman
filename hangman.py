def get_puzzle():
    pass

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    pass

def display_board(solved):
    pass

def show_result():
    pass
    
def play():
    pass
    
play()
