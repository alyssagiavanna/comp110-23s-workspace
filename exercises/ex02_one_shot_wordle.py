"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730519262"

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_box: str = " "
index_check: int = 0
winning_word: str = "python"
word_guess: str = input(f"What is your {len(winning_word)}-letter guess? ")

# check if word guessed is 6 letters? If not... try again. 
while(len(word_guess) != len(winning_word)):
    word_guess = input(f"That was not {len(winning_word)} letters! Try again: ")

# check if index is less than the winning word's length. 
while(index_check < len(winning_word)):
    # if the corresponding index of word guessed and winnning word is the same, show green square. 
    if(word_guess[index_check] == winning_word[index_check]):
        guess_box = guess_box + GREEN_BOX
    # if not, check if letter in guessed word exists elsewhere in the winning word. 
    else:
        char_exist: bool = False
        alternate_indices: int = 0
        # check if character exists elsewhere in the winning word and if the index is less than the number of letters in the winning word. 
        while(char_exist is not True and alternate_indices < len(winning_word)):
            # if the index in the winning word is equal to the index in the word guessed, change character elsewhere to true. 
            if(winning_word[alternate_indices] == word_guess[index_check]):
                char_exist = True
            # if not, go to the following index in the winning word and check if the character is in winning word and less than its index. 
            else:
                alternate_indices = alternate_indices + 1
        # if the character at a different index is in the winning word, show yellow square. 
        if(char_exist is True):
            guess_box = (guess_box + YELLOW_BOX)
        # if the character in the guessed word does not exist in the winning word, show white square. 
        else:
            guess_box = (guess_box + WHITE_BOX) 
    # if character at the corresponding index is not the same as the winning word, go to the following index in the gueassed word and check if the index is less than the number of letters in the winning word. 
    index_check = (index_check + 1)
# print results for each index of the guessed word. 
print(guess_box)
# if you guessed the winning word, print "Woo! You got it!" 
if(word_guess == winning_word):
    print("Woo! You got it!")
# if you did not guess the winning word, print "Not quite. Play again soon!" 
else:
    print("Not quite. Play again soon!")