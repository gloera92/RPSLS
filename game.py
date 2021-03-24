from player import Player


class Game:
    def __init__(self):
        self.player = Player()

    def run_game(self):
        self.welcome_message()
        self.display_rules()


    def welcome_message(self):
        print("Welcome to rock, paper, scissors, lizard, spock")

    def display_rules(self):
        print("Here are the Rules, choose your gesture wisely and guess what the opponent might pick!")

