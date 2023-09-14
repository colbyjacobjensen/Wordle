# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    correct_word = random.choice(FIVE_LETTER_WORDS) # Selects random word from WordleDictionary
    # letters = []  # Create an empty list to store the letters
    userGuess = []
    gw = WordleGWindow()

    # Loop to add letters from correct_word to list
    for letter in correct_word:
        letters.append(letter)

    letters = [letter.upper() for letter in letters]

    while userGuess not in FIVE_LETTER_WORDS:
        gw.add_enter_listener()
        gw.show_message("Not in word list.")

    # Milestone 1
    # for r in range(N_ROWS): 
    #     for c in range(N_COLS):
    #         gw.set_square_letter(r, c, letters[c])
    #         gw.get_square_letter(r,c)

    def enter_action(s):
        gw.show_message(letters)

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()