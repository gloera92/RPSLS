from player import Player


class Ai(Player):
    def __init__(self):
        self.player = "Bob"
        super().__init__()

    def create_name(self):
        print(f"Your opponents name is {self.player}")

    def player_gestures(self, name):
        self.player = "Bob"
        print(f'Select your gesture {self.player}:')
        print(f'Here are your gestures {self.gesture_list}')

    def player_gesture_choices(self):
        pass

    def gesture_selection(self, player_response):
        pass
