"""The Strange Man's House."""
__author__ = "730519262"

points: int = 0

player: str = ""


def main() -> None:
    global points
    greet()
    print("The overall idea is to get to at least 15 adventure points and I will let you be my friend. \nRight now you have " + str(points) + " points, but I will give you so many oppertunities to get more! \n*stranger starts laughing and breathing heavily*")
    user_imput: str = input("Type 1: \"I AM GONNA WIN!!!\" \nType 2: \"You are a really strange guy.3\" \nType 3: \"I am not a little kid who plays silly games.\"")
    
    if user_imput is "1":
        color()
    if user_imput is "2":
        print(f"Okay {player} if that is how you wanna play, we are gonna play the hard way. >:(")
        magic_number: int = int(input("Pick a number 1-100. "))
        points += math(magic_number)
    if user_imput is "3":
        print("Oh... okay... see you another time i guess. \n*stranger begins to shed a tear as you walk away*")
        print("GAME OVER.")
        return

def greet() -> None:

    name_select: str = input("Hello! Welcome to my lovely home.. eh basement. What is your name? \nType 1 to say: \'No way weirdo! Who are you?!\' or Type your name: ")

    if name_select == "1":
        name_select = "Mack"
        print("Alright I guess I will just have to call you Mack. You look like a Mack.")
    else:
        print(f"Well hello {name_select}. Ready to play a game?")
        global player
    player = name_select
    return 


def color() -> None:
    
    favorite_colors: dict[str, int] = {1:"red",2:"yellow",3:"blue",4:"green",5:"purple"}
    global player
    global points
   
    print("I am so glad you are excited! \nIn this game you have to guess my favorite color. Don't worry the color is not a complicated one... think of the regular colors!")
    guess: str = input("You have 5 tries and can win up to 15 points!")
    
    from random import randint
    favorite_color: str = favorite_colors[randint(1,8)]
    
    count_tries: int = 1
    possible_points: int = 15

    while guess != favorite_color and count_tries < 5:
        possible_points -= 3
        guess = input(f"Not quite. You have {5 - count_tries} tries left.")
        count_tries += 1

    if guess == favorite_color:
        print(f"SLAYY {player} !! You guessed it and won {possible_points} points!")
    else:
        possible_points -= 3
        print("Wow " + player + ". you really got no points. You are a pretty lame friend.")
        
    points += possible_points

Lock_hole: str = "\U00002B1C" 
keys: str = "\U0001F7E9"

def math(num:int) -> int:
    print("Now based on the number you picked, you have to guess the code to this locker.\nEach decifered lock is worth 1 point and my forgiveness for calling me strange.")
     
    globals
    Lock_hole
    keys

    idx: int = 0
    possible_points: int = 0
    count_trials: int = 1

    guess_box: str = ""
    while idx < len(guess_box):
        guess_box += Lock_hole    
        idx += 1
    
    coded_box: list[str] = ["\U00002B1C","\U00002B1C","\U00002B1C","\U00002B1C","\U00002B1C"]

    uncoded_box: list[int] = [8, 7, 0, 60, 82]
    prob_list: list[str] = ["36 / 12 + 7 - 2","2 * 30 / 12 + 2","4 ** 2 - 2 **6","(504 - 84) / 7","45 * 3 ** 2 / 37 + 1"]

    i: int = 0

    if num > 50:
        print(f"Solve a series of math problems in order to unlock each white square. {guess_box}")

        idx: int = 0
        while count_trials <= len(guess_box):
            answer: float = input(f"Problem {count_trials}: \n{prob_list[i]}")
            if answer == uncoded_box[i]:
                coded_box[i] == keys 
                possible_points +=1
                print(coded_box)
            i += 1
            count_trials += 1

    prob2_list: list[str] = ["How many legs does a squid have?","How many \'deadly sins\' are there?","What is the freezing temperature in Celcius?","How many minutes will it take me to get home if I live 3 mile away amd am going 3 mile an hour","8 friends go to a resteraunt and there meals cost $20.50 each. How much money total was spent?"]

    if num < 50:
        idx: int = 0
        while idx < len(guess_box):
            guess_box = guess_box + locks

        print(f"In order to unlock each white square, you must correctly answer each question. \n{guess_box}")
        
        while count_trials <= len(guess_box):
            answer: float = input(f"Problem {count_trials}: \n{prob2_list[i]}")
            if answer == uncoded_box[i]:
                coded_box[i] == keys 
                possible_points +=1
                print(coded_box)
            i += 1
            count_trials += 1
    return possible_points

if __name__ == "__main__":
  main()

