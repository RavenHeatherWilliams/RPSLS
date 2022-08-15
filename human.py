from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        self.gesture = Player("rock, paper, scisors, lizard, spock")
    
    def battle(self,AI):
        AI.gesture -= self.gesture.user_choice
        print(f'AI has selected {self.gesture} and {self.gesture.user_choice}')


