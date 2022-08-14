from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.human = Human
        self.ai = AI

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to ROCK PAPER SCISSORS LIZARD SPOCK!")

        # self.rock
        # self.scissors
        # self.paper
        # self.spock
        # self.lizard