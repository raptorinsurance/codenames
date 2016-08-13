import kivy
kivy.require('1.9.1')

from kivy.app import App
from codenames_game import CodenamesGame
from kivy.config import Config
Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 750)

class CodenamesApp(App):

    def build(self):
       game = CodenamesGame()
       game.play()
       return game

if __name__ == "__main__":
    CodenamesApp().run()
