import unittest
import bowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testOneSpare(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            # change rolls to roll as roll is the function to call
            self.game.roll(pins)
