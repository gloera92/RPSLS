from player import Player
from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player = Player()
        self.playerOne = Human()
        self.playerTwo = Ai()
        self.game_mode = ['Computer', 'Multiplayer']

    def run_game(self):
        self.welcome_message()
        self.display_rules()
        self.game_mode_selected(self.game_type())
        self.player.player_gestures(self.player.create_name())
        self.playerTwo.player_gestures(self.playerTwo.create_name())
        self.player.gesture_selection(self.player.player_gesture_choices())
        self.playerTwo.gesture_selection(self.playerTwo.player_gesture_choices())


    def welcome_message(self):
        print("Welcome to rock, paper, scissors, lizard, spock")

    def display_rules(self):
        print("Here are the Rules, choose your gesture wisely and guess what the opponent might pick!")

    def game_type(self):
        print("Please select which Game Mode you would like to play")
        i = 0
        while i < len(self.game_mode):
            print(f'Press {i} for {self.game_mode[i]}')
            i += 1

        selection = input()
        return int(selection)

    def game_mode_selected(self, game_type):
        if self.game_mode[game_type] == self.game_mode[0]:
            print(f'You chose to vs {self.game_mode[game_type]}')
            return self
        else:
            print(f'{self.game_mode[game_type]} selected')
            return self




