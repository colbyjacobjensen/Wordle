# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    gw = WordleGWindow()
    correct_word = random.choice(FIVE_LETTER_WORDS) # Selects random word from WordleDictionary
    letters = []  # Creates an empty list to store the letters of the correct word
    
    # Loop to add letters from correct_word to list
    for letter in correct_word:
        letters.append(letter)

    letters = [letter.upper() for letter in letters] # Capitalizes letters in array

    # Milestone 1 (Complete)
    # for r in range(N_ROWS): 
    #     for c in range(N_COLS):
    #         gw.set_square_letter(0, c, letters[c])
    #         gw.get_square_letter(0,c)

    def enter_action(s):
        userGuess=[]

        for c in range(N_COLS):
            userGuess.append(gw.get_square_letter(0,c)) 

        userGuess = [letter.lower() for letter in userGuess]
        word = ''.join(userGuess)

        if word not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            gw.show_message("In word list")

    gw.add_enter_listener(enter_action)
    
    
# Startup code

if __name__ == "__main__":
    wordle()