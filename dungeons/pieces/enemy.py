"""Enemy code.

This file was created on July 27, 2021
"""
from dungeons.geometry.directions import Direction


class Enemy(object):
    """A class to represent a player in the dungeon."""

    def __init__(self, x: int, y: int, threat_level: int = 1) -> None:
        """Init function for the Player class.

        Args:
            x (int): X location.
            y (int): Y location.
            threat_level (int): Enemy threat level.
        """
        self._x: int = x
        self._y: int = y
        self._threat_level: int = threat_level

    @property
    def x(self) -> int:
        """Players x location."""
        return self._x

    @property
    def y(self) -> int:
        """Players y location."""
        return self._y

    def move(self, direction: Direction) -> None:
        """Move the players current position.

        Args:
            direction (Direction): The direction the player should move.
        """
        self._x = self.x + direction.x
        self._y = self.y + direction.y
