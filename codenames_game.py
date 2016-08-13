from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from card_grid import CardGrid

class CodenamesGame(Widget):
    card_grid = ObjectProperty(None)

    def play(self):
        self.setup()

    def setup(self):
        self.card_grid.setup()


