from kivy.uix.widget import Widget
from kivy.properties import ListProperty

from card import Card


class CardGrid(Widget):
    cards = ListProperty()

    def setup(self):
        words = "abcdefghijklmnopqrstuvwxy"
        for i in range(25):
            card = Card()
            card.setWord(words[i])
            self.ids.grid.add_widget(card)
            self.cards.append(card)
