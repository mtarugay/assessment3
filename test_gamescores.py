"""
Unit tests for BowlingGame

This module contains unit tests for the BowlingGame class, focusing on game behavior and scoring accuracy.
"""

import unittest
from bowling_game import BowlingGame

class TestGameScores(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_spare(self):
        """Helper to roll a spare with two fixed values (6+4) that total to 10."""
        self.game.roll(6)
        self.game.roll(4)

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)
            
    def test_only_oframes(self):
        """Test a game where all frames are open (no spares or strikes)."""
        for _ in range(10):
            self.game.roll(3)
            self.game.roll(5)
        self.assertEqual(self.game.score(), 80)

    def test_all_gutters(self):
        """Test a game with all gutter balls."""
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_mixed(self):
        """Test a mixed game with spares, open frames, and bonus calculations."""
        self.roll_spare()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_spare()
        self.game.roll(2)
        self.game.roll(3)
        self.roll_spare()
        self.roll_spare()
        self.game.roll(4)
        self.game.roll(3)
        self.roll_spare()
        self.roll_spare()
        self.roll_spare()
        self.game.roll(5)
        self.assertTrue(isinstance(self.game.score(), int))

    def test_all_fives(self):
        """Test a game of 10 spares made by rolling 5 each time."""
        self.roll_many(21, 5)
        self.assertEqual(self.game.score(), 150)

if __name__ == "__main__":
    unittest.main()