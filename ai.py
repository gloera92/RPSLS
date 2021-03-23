from player import Player
from gestures import Gestures


class Ai(Player):
    def __init__(self):
        self.gestures = Gestures
        super().__init__()

    def ai_gesture(self):
        self.ai = Gestures.gestures()
