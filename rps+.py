# -------------------------------------- STAGE 5 / 5 -------------------------------------- #
from random import choice
from sys import exit


print("""\nWelcome to ROCK-PAPER-SCISSORS++ !!
You can play the ORIGINAL game or chose other things to play with!

QUICK-TOUR:
--------------------------------------
the game goes on forever! Unless you:
type '!exit' to finish the program

by typing '!rating' you get your score!
    +100 for a WIN!
    +50 for a draw!
    +0 for a lose!
--------------------------------------

further you'll be able to set the game!
for now, type your name!
""")

# getting user's name
name = input("Enter your name: ")
print('===========================================')
print(f"\nHello, {name}\n")

# transforming into a dict mapping names to ratings
with open('rating.txt', 'r') as rating:
    temp_list = rating.readlines()
    rate_dict = {}
    for i, elem in enumerate(temp_list):
        e = elem.split()
        rate_dict[e[0]] = int(e[1])
    del temp_list

# checks for user's score
if name in rate_dict:
    score = rate_dict[name]
else:
    score = 0

# game logic
game = {
    # option: l o s e s     f o r    7    o t h e r
    "rock": ["gun", "lightning", "devil", "dragon", "water", "air", "paper"],
    "gun": ["lightning", "devil", "dragon", "water", "air", "paper", "sponge"],
    "lightning": ["devil", "dragon", "water", "air", "paper", "sponge", "wolf"],
    "devil": ["dragon", "water", "air", "paper", "sponge", "wolf", "tree"],
    "dragon": ["water", "air", "paper", "sponge", "wolf", "tree", "human"],
    "water": ["air", "paper", "sponge", "wolf", "tree", "human", "snake"],
    "air": ["paper", "sponge", "wolf", "tree", "human", "snake", "scissors"],
    "paper": ["sponge", "wolf", "tree", "human", "snake", "scissors", "fire"],
    "sponge": ["wolf", "tree", "human", "snake", "scissors", "fire", "rock"],
    "wolf": ["tree", "human", "snake", "scissors", "fire", "rock", "gun"],
    "tree": ["human", "snake", "scissors", "fire", "rock", "gun", "lightning"],
    "human": ["snake", "scissors", "fire", "rock", "gun", "lightning", "devil"],
    "snake": ["scissors", "fire", "rock", "gun", "lightning", "devil", "dragon"],
    "scissors": ["fire", "rock", "gun", "lightning", "devil", "dragon", "water"],
    "fire": ["rock", "gun", "lightning", "devil", "dragon", "water", "air"]
}

print("You can choose to play with the choices from this list:")
print(list(game.keys()))
print("\nYou can type 'all' if you want all of 'em!")
print("\nOr press enter to play original ROCK-PAPER-SCISSORS\n")

option = input().split(',')
option = option if option != [''] else []

# If user hits enter, then user == ['']
if not option:
    del game  # Deletes the complex rock_paper_scissors+
    game = {
        # option: loses for
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
elif option == ['all']:
    pass
# if user enters options to play
else:
    # deletes all other options leaving only user's options to play
    temp_dict = game.copy()
    for key in temp_dict:
        if key not in option:
            del game[key]

print("Okay, let's start")

# Keeps going till a `break` or an `exit` is reached
while 1:
    while 1:
        user = input()
        if user in game:  # that is, if user == "rock" or "paper" or "scissors"
            break  # breaks from inner infinite loop
        elif user == "!exit":
            print("Bye!")
            exit(0)  # exits the whole program!
        elif user == "!rating":
            print(f"Your rating: {score}")
        else:
            print("Invalid input")  # else, means the user inputted a wrong string!

    # comp chooses from list of game.keys()
    comp = choice(list(game.keys()))

    # If user == comp then DRAW
    if user == comp:
        score += 50
        print(f"There is a draw ({user})")
    # if user == conjugate of comp's choice, then means comp loses!!
    elif user in game[comp]:
        score += 100
        print(f"Well done. The computer chose {comp} and failed")
    # Anything different from that, means the comp Wins!
    else:
        print(f"Sorry, but the computer chose {comp}")
        
