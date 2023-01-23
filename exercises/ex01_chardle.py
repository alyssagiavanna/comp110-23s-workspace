"""EXO - Chardle - A cute step toward Wordle."""
__author__ = "730519262"

word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
print("Searching for " + character + " in " + word)
if (len(character) != 1):
    print("Error: Character must be a single character")
    exit()

number_of_match: int = 0

if (character == word[0]):
    print(character + " found at index 0")
    number_of_match = number_of_match + 1

if (character == word[1]):
    print(character + " found at index 1")
    number_of_match = number_of_match + 1

if (character == word[2]):
    print(character + " found at index 2")
    number_of_match = number_of_match + 1

if (character == word[3]):
    print(character + " found at index 3")
    number_of_match = number_of_match + 1

if (character == word[4]):
    print(character + " found at index 4 ")
    number_of_matchatch = number_of_match + 1

if (number_of_match == 0):
    print("No instances of " + character + " found in " + word)

if (number_of_match == 1):
    print(str(number_of_match) + " instance of " + character + " found in " + word)

else: 
    print(str(number_of_match) + " instances of " + character + " found in " + word)

