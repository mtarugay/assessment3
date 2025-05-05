"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""

class BowlingGame:
    def __init__(self):
        """
        Initializes a new game with 10 frames. 
        Each frame has up to 2 rolls (except the 10th frame which can have 3 rolls).
        """
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins (int): The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """
        Calculates the score for the current game. The score is calculates based on the results of the
        then games ran

        Returns:
            int: The calulated total score.
        """
        score = 0
        frame_index = 0
        frames_scored = 0  # Added to track scored frames
        while frames_scored < 10:  # To ensure only 10 frames per game.
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
            frames_scored += 1  #  Added for frame checking

        return score

    def _is_strike(self, frame_index):
        """
        Checks if the roll at frame_index is a strike.

        Args:
            frame_index (int): Index of the roll to check.

        Returns:
            bool: True if the roll is 10, if not then False.
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Checks if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index (int): Index of the first roll in a frame.

        Returns:
            bool: True if the rolls add up to 10/spare, if not then False.
        """
        return (frame_index + 1 < len(self.rolls) and
                self.rolls[frame_index] + self.rolls[frame_index + 1] == 10)

    def _strike_bonus(self, frame_index):
        """
        Calculates the bonus for a strike.

        Args:
            frame_index (int): Index of the strike roll.

        Returns:
            int: The value of the next two rolls after the strike.
        """
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """
        Calculates the bonus for a spare.

        Args:
            frame_index (int): Index of the first roll in a spare.

        Returns:
            int: The value of the roll after the spare.
        """
        return self.rolls[frame_index + 2]
