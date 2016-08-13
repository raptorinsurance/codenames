import unittest
import unittest.mock as mock
from kivy.base import EventLoopBase

from codenames_game import CodenamesGame


class TestCodenamesGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_patches = [
            mock.patch('kivy.uix.widget.Builder'),
            mock.patch.object(EventLoopBase, 'ensure_window', lambda x: None),
        ]
        for patch in cls.mock_patches:
            patch.start()

    @classmethod
    def tearDownClass(cls):
        for patch in cls.mock_patches:
            patch.stop()
