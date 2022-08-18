class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        self.chosen_gesture = ""
        self.wins = 0

    def choose_gesture(self):
        user_choice = int(input("Press 0 to select rock, 1 for paper, 2 for scissors, 3 for lizard or 4 for spock"))
        self.chosen_gesture = self.gesture_list[user_choice]
        print(f'{self.name} has selected {self.chosen_gesture}')
        

    # def gesture_user_choice(self):
 

