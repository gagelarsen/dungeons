"""Direction class to be used by the dungeon generator.

This file was generated on June 04, 2020
"""


class Direction(object):
    """A class to hold information about directions used the dungeon generator."""
    def __init__(self, x: int, y: int) -> None:
        """
        __init__ function for the Direction class.

        Args:
            x: The direction x.
            y: The direction y.
        """
        self.x = x
        self.y = y


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)

NORTH = Direction(0, -1)
SOUTH = Direction(0, 1)
WEST = Direction(-1, 0)
EAST = Direction(1, 0)
NORTHWEST = Direction(-1, -1)
SOUTHWEST = Direction(-1, 1)
NORTHEAST = Direction(1, -1)
SOUTHEAST = Direction(1, 1)

DPAD_DIRECTIONS = [
    UP,
    DOWN,
    LEFT,
    RIGHT,
]

CARDINAL_DIRECTIONS = [
    NORTH,
    SOUTH,
    EAST,
    WEST,
    NORTHWEST,
    SOUTHWEST,
    NORTHEAST,
    SOUTHEAST,
]
