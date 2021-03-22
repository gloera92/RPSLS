from gestures import Gestures
from player import Player


class Human(Player):
    def __init__(self):
        self.gesture = Gestures()
        super().__init__()
