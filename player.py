

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
            return self.gesture_list
        else:
            print("try again")

    def game_play(self, player_one, player_two):
        if player_one != player_two:
            print("tied")
        else:
            return


playerOne = Player()
playerOne.player_gestures(playerOne.create_name())
playerOne.gesture_selection(playerOne.player_gesture_choices())
playerTwo = Player()
playerTwo.player_gestures(playerTwo.create_name())
playerTwo.gesture_selection(playerTwo.player_gesture_choices())
playerResult = playerOne and playerTwo
playerResult.game_play(playerOne, playerTwo)




