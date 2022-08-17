from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None

    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.battle()
        # self.display_winner()

    def display_welcome(self):
        print("Welcome to ROCK PAPER SCISSORS LIZARD SPOCK!")
        print("Each match will be best of three games!")
        print("Use the number keys to enter your selection")

    def choose_game_mode(self):
        user_choice = input("press 1 for single player, 2 for multi player")
        if user_choice == "1":
            self.player_one = Human("human")
            self.player_two = AI("rumba")
        elif user_choice == "2":
            self.player_one = Human("Human one")
            self.player_two = Human("Human two")

        
               # check to see if its a tie, check all condions for player one win "else" player 2 is the winner
    def battle(self):
        # while self.player_one.wins is less than 2 AND self.player_two.wins is less than 2:
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("its a tie, keep playing")
        elif self.player_one.choose_gesture == "Rock" and self.player_two.choose_gesture == "Scissors":
            print("player one wins this hand")
            self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Paper" and self.player_two.choose_gesture == "Rock":
            self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Scissors" and self.player_two.choose_gesture == "Paper":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Rock" and self.player_two.choose_gesture == "Lizard":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Lizard" and self.player_two.choose_gesture == "Spock":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Spock" and self.player_two.choose_gesture == "Scissors":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Scissors" and self.player_two.choose_gesture == "Lizard":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Lizard" and self.player_two.choose_gesture == "Paper":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Paper" and self.player_two.choose_gesture == "Spock":
             self.player_one.wins =+ 1
        elif self.player_one.choose_gesture == "Spock" and self.player_two.choose_gesture == "Rock":
             self.player_one.wins =+ 1
        # continue adding elif here
        else:
            print("player two wins this hand")
            self.player_two.wins += 1
