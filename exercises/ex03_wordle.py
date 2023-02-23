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
        if word[idx_1] == one_letter:
            return True
        else: 
            idx_1 = idx_1 + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Testing for yellow or white box codification"""
    assert len(guess) == len(secret)
    idx_2: int = 0
    guess_box: str = " "
    
    while idx_2 < len(guess):
    #while the index is less than the length of guess word    
        if (guess[idx_2] == secret[idx_2]):
        #if the guess word contains a letter in from the secret word and they are in the same index return green emoji box
            guess_box = guess_box + GREEN_BOX
        elif (contains_char(secret,guess[idx_2]) is True):
        #if the guess word contains a letter in from the secret word and they are not in the same index return yellow emoji box    
            guess_box = guess_box + YELLOW_BOX
        else:
        #if the guess word contains no letters in the secret word return white emoji box
            guess_box = guess_box + WHITE_BOX
        idx_2 = idx_2 + 1
    return guess_box

def input_guess(word_length: int) -> str:
    """vgjasvhcdsakfBKa"""
    first_guess: str = input(f"Enter a {word_length} character word: ")

    while len(first_guess) != word_length:
        first_guess = input(f"That wasn't {word_length} chars! Try again: ")
    return first_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    trial: int = 1
    try_again: bool = False

    while (trial <= 6) and (try_again is False):
        print(f"=== Turn {trial}/6 ===")
        #tells player how many trys left
        player_guess: str = input_guess(len(secret))
        print(emojified(player_guess,secret))
        if player_guess == secret:
            print(f"You won in {trial}/6 turns!")
            try_again = True
        else:
            trial = trial + 1
    
    if try_again == False:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()