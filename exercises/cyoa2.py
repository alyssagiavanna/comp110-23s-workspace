"""What kind of fruit are you?"""
__author__ = "730519262"

player: str = ""
points: int = 0
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    globals
    points
    YELLOW_BOX

    greet()
    print(f"The overall idea is to get as many points as possible to win different prizes! \nRight now you have {points} points, but you will have so many chances to win! \nEach time you get up to 10 points, you will recieve a yellow box. Each one contains a super special prize. You got to play to win if you want them all!")
    player_choices: input("So what is gonna be. You can either start playing the game for your first 5 points or if you want to take a risk you can go straight to our \'Fun and Fortune\' round to try and win 10 points earning you your first yellow box! \nRespond with, 1:\'Let's just start the normal game.\' 2:\'I AM READY FOR FUN AND FORTUNE\' 3:\'I still do not want a car or tp play this at all\'")
    prize: str = ""

    if player_choices == "1":
        round_one()
        if points >= 10:
            prize += YELLOW_BOX
            print(f"You have won your very first yellow_box! {prize}")
    if player_choices == "2":
        fun_and_fortune()
        if points >= 10:
            prize += YELLOW_BOX
            print(f"You have won your very first yellow_box! {prize}")
            recieve_prize(points)
    if player_choices == "3":
        print(f"Well it seems you are leaving here with {points} points and no prizes. Come back if you want to play another time!")
        



def greet() -> None:

    name_select: str = input("Hello! Welcome to the game where you want the most points to win a brand new car. What is your name? \nType 1 to say: \'I don't want a car.\' or Type your name: ")

    if name_select == "1":
        name_select = "Mack"
        print("Alright I guess I will just have to call you Mack. Get ready to play for the win Mack!")
    else:
        print(f"Well hello {name_select}. Get ready to play for the win!")
        global player
    player = name_select
    return 


def round_one() -> None:
    print("Welcome to Round One! I hope you are good at math because this game is all about numbers. \nYou will be given 5 math problems and for each one you solve correctly, you get one point.")

    globals
    points

    prob_list: list[str] = ["36 / 12 + 7 - 2","2 * 30 / 12 + 2","4 ** 2 - 2 **6","(504 - 84) / 7","45 * 3 ** 2 / 37 + 1"]
    answer_key: list[int] = [8, 7, 0, 60, 82]
    i: int = 0
    trials: int = 1
    possible_points: int = 0
    
    while trials <= len(prob_list):
        answer: float = input(f"Problem {trials}: \n{prob_list[i]}")
        if answer == answer_key[i]:
            print("Correct! You have won a point!")
            possible_points += 1
        else:
            print("Wrong answer. wamp wamp.")
        trials += 1
        i += 1
    
    if possible_points < 0:
        print(f"Congradulations! You won {possible_points} points!")
        points = possible_points
        if possible_points == 5:
            print("Since you recieved all 5 possible points! You win an extra 2 points for great effort!")
            points +=2
    else:
        print("Looks like this was anot your best round. No points were won.") 


def fun_and_fortune() -> None:
    print("Welcome to Fun and Fortune! Seems like you have taken a leap of faith. This round is based on instinct alone. \nThere are 5 colors in a jar: red, yellow, blue, green, and purple. You will be given only 3 tries to guess the color that has been pulled from the jar. If you guess it you will win 10 points and a prize!")

    colors: dict[str, int] = {1:"red",2:"yellow",3:"blue",4:"green",5:"purple"}
    global player
    global points

    from random import randint
    color: str = colors[randint(1,8)]
    tries: int = 3
    possible_points: int = 0

    print("The color has been picked.")

    while tries > 0 and guess != color:
        guess: str = input(f"You have {tries} to guess")
        if guess == color[tries] and tries == 3:
            print("Wow! That is some luck. You just won yourself an extra 3 points.")
            possible_points += 13
        if guess == color[tries] and tries == 2:
            print("That is correct! 10 points for you.")
            possible_points += 10
        if guess == color[tries] and tries == 1:
            print("That was pretty close, but hey you got it! 10 lucky points.")
            possible_points += 10
        if guess != color[tries]:
            print("Sorry, but that's not it.")
        tries += 1

    if possible_points == 0:
        print(f"Unfortunately you won {possible_points} points.")
    else:
        print(f"Congradulations! You guessed right and won {possible_points} points!")

    points = possible_points


def recieve_prize(points_won: int) -> int:

    globals
    points

    if points_won >= 10 and points_won < 20:
        print("Your very first prize won is a.... GOLDFISH!")
    
    if points_won >= 20 and points_won < 30:
        print("Two prizes! Never guessed you would get that many... anyway here is a gift certificate to McDonalds.")