import kivy
kivy.require('1.9.1')

from kivy.app import App
from codenames_game import CodenamesGame

class CodenamesApp(App):
    def build(self):
       game = CodenamesGame()
       return game

if __name__ == "__main__":
    CodenamesApp().run()
