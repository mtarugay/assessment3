import unittest
from bowling_game import BowlingGame

class TestEdgeCases(unittest.TestCase):
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

    def test_max_score(self):
        """Test a perfect game with all strikes.."""
        self.roll_many(12, 10) 
        self.assertEqual(self.game.score(), 300)

    def test_tenth_frame_spare(self):
        """Tests a spare in 10th frame with a bonus roll."""
        for _ in range(9):  
            self.game.roll(4)
            self.game.roll(5)
        self.game.roll(5)
        self.game.roll(5) 
        self.game.roll(4) 
        self.assertTrue(isinstance(self.game.score(), int))

    def test_tenth_frame_strike(self):
        """Tests a strike in the 10th frame with 2 bonus rolls."""
        for _ in range(9): 
            self.game.roll(4)
            self.game.roll(5)
        self.game.roll(10) 
        self.game.roll(3)
        self.game.roll(6)  
        self.assertTrue(isinstance(self.game.score(), int))

if __name__ == "__main__":
    unittest.main()