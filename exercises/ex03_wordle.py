"""EX03 - Structured Wordle"""
__author__ = "730519262"

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, one_letter: str) -> bool:
    """Returns True if letter is in the word and False if not"""
    assert len(one_letter) == 1
    idx_1: int = 0

    while idx_1 < len(word):
    #making sure the index doesnt go outside of the word's highest index  
        if word[idx_1] == one_letter:
            return True
        #checking if letter is at each index
        else: 
            idx_1 = idx_1 + 1
        #continues looking through each of the word's indexes
    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Testing for green or yellow or white box codification"""
    assert len(guess_word) == len(secret_word)
    idx_2: int = 0
    guess_box: str = " "

    while idx_2 < len(guess_word):
    #while the index is less than the length of guess word    
        if (guess_word[idx_2] == secret_word[idx_2]):
        #if the letter in the guess word's index and the secret word's index are the same return green emoji box
            guess_box = guess_box + GREEN_BOX
        elif (contains_char(secret_word,guess_word[idx_2]) is True):
        #if the guess word contains a letter in the secret word and they are not in the same index return yellow emoji box    
            guess_box = guess_box + YELLOW_BOX
        else:
        #if the guess word contains no letters in the secret word return white emoji box
            guess_box = guess_box + WHITE_BOX
        idx_2 = idx_2 + 1
        #continues looking through for each index
    return guess_box

def input_guess(word_length: int) -> str:
    """Making sure the word guessed matches the length of letters in the inputed word"""
    first_guess: str = input(f"Enter a {word_length} character word: ")

    while len(first_guess) != word_length:
    #while the length of the guess word does not equal the length of the inputed word
        first_guess = input(f"That wasn't {word_length} chars! Try again: ")
        #tells user it is not the correct amount of characters in the word and asks to submit a new word
    return first_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "zoinks"
    trial: int = 1
    try_again: bool = False

    while (trial <= 6) and (try_again is False):
    #while the player is within the max 6 tries and has not guessed the secret word, game continues
        print(f"=== Turn {trial}/6 ===")
        #tells player how many tries left
        player_guess: str = input_guess(len(secret))
        #prompts player to guess a word
        print(emojified(player_guess, secret))
        #shows player the enoji hint to the secret word's characters
        if player_guess == secret:
            print(f"You won in {trial}/6 turns!")
            try_again = True
        #player guesses word and game is over
        else:
            trial = trial + 1
        #player incorrectly guesses word and has one less try than before
    
    if try_again == False:
        print("X/6 - Sorry, try again tomorrow!")
    #player has run out of tries and loses the game

if __name__ == "__main__":
    main()