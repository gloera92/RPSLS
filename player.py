

class Player:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.player = ''
        self.score = 0
        self.choice = ''

    def create_name(self):
        print("Please select a player name")
        response = input()
        return response

    def player_gestures(self, player_name):
        print(f'Select your gesture {player_name}:')
        print(f'Here are your gestures {self.gesture_list}')

    def player_gesture_choices(self):
        i = 0
        while i < len(self.gesture_list):
            print(f'Press {i} for {self.gesture_list[i]}')
            i += 1

        response = input()
        return int(response)

    def gesture_selection(self, player_response):
        i = player_response
        if self.gesture_list[i] == self.gesture_list[i]:
            print(f"You chose {self.gesture_list[i]}!")
        else:
            print("try again")


playerOne = Player()
playerOne.player_gestures(playerOne.create_name())
playerOne.gesture_selection(playerOne.player_gesture_choices())


