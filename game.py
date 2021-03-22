from gestures import Gestures


class Game:
    def __init__(self):
        self.gestures = Gestures()

    def run_game(self):
        self.welcome_message()
        self.display_rules()


    # game code goes here


    def welcome_message(self):
        print("Welcome to rock, paper, scissors, lizard, spock")

    def display_rules(self):
        print("Here are the Rules, choose your gesture wisely and guess what the opponent might pick!")

    def choose_gesture(self, gesture):
        print(f"Choose your {gesture}")
        # enter a number 1-5 for gesture
        i = 0
        while i < len(self.gestures.gesture_list.append(gesture[i])):
            print(f'Press {i} for {self.gestures.gesture_list.append[i]}')

        response = input()
        return int(response)
