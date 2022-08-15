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
        print("Each match will be best of three games!")
        print("Use the number keys to enter your selection")
        
               
    # def self.battle(self):
