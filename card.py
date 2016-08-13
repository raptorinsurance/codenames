from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Card(Widget):
    word = StringProperty()

    def setWord(self, word):
        self.word = word
        self.ids.button.text = word

