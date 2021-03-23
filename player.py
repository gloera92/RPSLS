

class Gestures:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


class Player(Gestures):
    def human_gestures(self):
        print(f'Select your gesture:')
        print(f'Here are your gestures {self.gesture_list}')
        print(f'0 = rock, 1 = paper, 2 = scissors, 3 = lizard 4 = spock')
        response = input()
        return int(response)

    def human_choice(self, player_input):
        i = player_input
        if self.gesture_list[i] == self.gesture_list[i]:
            print(f'You chose {self.gesture_list[i]}')
        else:
            print('try again')
