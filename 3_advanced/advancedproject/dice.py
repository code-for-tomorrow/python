# Daniel likes to get together with his friends every week on a
# random day to play dice. In his game of dice, the objective is
# to see who gets three of the same number first.

# Algorithm Description: Use a class to represent a player. Create a
# turn log (using 2d list with each inner list containing the outcomes
# for all players representing a turn. Ex: [[1,2,4],[4,2,6]] ).
# Create a dictionary (that is an instance variable of the player
# class) to keep track of how many of each dice outcome each
# person playing the game got. For example, Daniel’s outcomes can
# look like {1:2, 2:3, 3:1, 4:0, 5:1, 6:2}. Once a person gets 3
# of the same outcome, a unique statement will be created
# (the statement should be like "Player x won").
# If multiple people won, it should be like "Player x, y won"

# Follow these steps to create this algorithm.
# 1) Import the random module which we will be using later.

# 2) Create a main class with
# --- instance variable in init: that asks the user for how many
# players and creates that many player classes
# --- instance variable in init: holding a list containing player
# (which is a class covered in the next section) instances based
# on how much the user inputted(so if user says 2 players playing,
# there should be 2 player instances in this list).
# --- instance variable in init: holding a turn log that should
# take each player's result each round (see in algorithm description)
# --- instance variable in init: holding the winners for this game
# --- instance variable in init: holding whether this game is over
# or not.
# --- a 'round' method that simulates one round of the game. so all
# the players should roll a random outcome(more in section 3).
# remember, every round, the turn log should be updated.
# also, check if the game has been won, and if it has, update the
# list containing the winners and the variable containing whether
# the game has been won.

# 3) Create a player class with
# --- instance variable in init: holding the random dice outcome
# for the player for this round
# --- instance variable in init: holding a dictionary that
# stores how many times they got each outcome
# --- instance variable in init: that tracks whether the
# player has rolled 3 of the same thing(in other words won) or not.
# --- a 'roll' method that determines the random outcome for the player
# (dice: a random int between 0 and 6 inclusive) and also whether the
# player won this round or not.

# At the end run the main class by doing main(). Running main()
# should print the turn log and print which player(s) won.

import random


class main:
    def __init__(self):
        self.playercount = int(input("How many players are playing?  "))
        self.turnlog = []
        self.players = [player() for i in range(self.playercount)]
        self.winners = []
        self.over = False

        print(
            "Note: player 0 is the first player, "
            + "player 1 is the second player, etc"
        )
        while not self.over:
            self.round()
        print("This is the record of the game")
        print(self.turnlog)
        print("Player(s)", str(self.winners).lstrip("[").rstrip("]"), "won")

    def round(self):
        for i in range(self.playercount):
            self.players[i].roll()
            if self.players[i].win:
                self.winners.append(i)
                self.over = True
        self.turnlog.append(
            [self.players[x].thisround for x in range(self.playercount)]
        )


class player:
    def __init__(self):
        self.thisround = None
        self.outcomes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.win = False

    def roll(self):
        self.thisround = random.randint(1, 6)
        self.outcomes[self.thisround] += 1
        if 3 in self.outcomes.values():
            self.win = True


letsplay = main()
