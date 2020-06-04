"""The dungeon class file.

This file was generated on June 03, 2020
"""
__author__ = "Gage Larsen"
__copyright__ = "Copyright: gagelarsen 2020"
__maintainer__ = "Gage Larsen"
__email__ = "gagelarsen53@gmail.com"

import random

from dungeons.geometry import directions
from dungeons.geometry.rectangle import Rectangle


class Dungeon(object):
    """A class to contain all the information about a dungeon that will be generated."""

    DUNGEON_ROOM = ' '
    DUNGEON_HALL = ' '
    DUNGEON_WALL = 'X'

    def __init__(self, width, height, random_seed=None, room_attempts=100,
                 max_room_width=10, max_room_height=10, min_room_width=5,
                 min_room_height=5):
        """The __init__ function for the Dungeon class."""
        self._width = width
        self._height = height
        self._room_attempts = room_attempts
        self._max_room_width = max_room_width
        self._min_room_width = min_room_width
        self._max_room_height = max_room_height
        self._min_room_height = min_room_height
        self.dungeon = []  # This is in the form dungeon[y][x]

        self._dungeon_rectangle = Rectangle(width=self._width, height=self._height)
        self.rooms = []

        if random_seed is not None:
            random.seed(random_seed)

        # Fill the Dungeon Array
        for _ in range(self._height):
            row = [self.DUNGEON_WALL for _ in range(self._width)]
            self.dungeon.append(row)

        # Add Rooms
        self._generate_rooms()

        # Add Passages
        self._carve_passages()

    @property
    def width(self):
        """The width of the dungeon."""
        return self._width

    @property
    def height(self):
        """The height of the dungeon."""
        return self._height

    def _set_dungeon_cell(self, x, y, value):
        """A function to set the value of a specified dungeon cell.

        Args:
            x: The specified x coordinate.
            y: The specified y coordinate.
            value: The new value of the cell.
        """
        self.dungeon[y][x] = value

    def _get_dungeon_cell(self, x, y):
        """A function to get the value of a specified dungeon cell."""
        return self.dungeon[y][x]

    def _generate_rooms(self):
        """A function to generate random rooms."""
        for _ in range(self._room_attempts):
            # Get Random Dimensions for New Room
            x = random.randint(1, self._width - 1)
            y = random.randint(1, self._height - 1)
            room_width = random.randint(self._min_room_width, self._max_room_width)
            room_height = random.randint(self._min_room_height, self._max_room_height)
            new_room = Rectangle(width=room_width, height=room_height, x=x, y=y)

            # Make sure the room doesn't overlap other rooms
            overlaps = False
            for room in self.rooms:
                if room.overlaps(new_room):
                    overlaps = True
                    break

            in_dungeon = False
            if not (not self._dungeon_rectangle.contains(new_room.x, new_room.y) or not
                    self._dungeon_rectangle.contains(new_room.x_max, new_room.y_max)):
                in_dungeon = True
            if not overlaps and in_dungeon:
                self.rooms.append(new_room)
        # Add Rooms to Dungeons
        for room in self.rooms:
            for x in range(room.x, room.x + room.width):
                for y in range(room.y, room.y + room.height):
                    self._set_dungeon_cell(x, y, self.DUNGEON_ROOM)

    def _carve_passages(self):
        """A function to carve passages in the maze."""
        # Loop through the dungeon to create maze.
        for y in range(1, self._height):
            for x in range(1, self._width):
                self._carve_passage_helper(x, y)

    def _carve_passage_helper(self, start_x, start_y):
        """A helper for carving the dungeon passages.

        Args:
            start_x: the starting x coordinate for the passageway.
            start_y: the starting y coordinate for the passageway.
        """
        if not self._can_carve_passage(start_x, start_y):
            return

    def _can_carve_passage(self, x, y):
        """Determine if a passage can be carved at a specified location in the dungeon.

        Args:
            x: the x coordinate of the cell to check
            y: the y coordinate of the cell to check

        Returns:
            True if the cell can be carved, or false if it cannot.
        """
        # Make sure the section is a wall
        if self._get_dungeon_cell(x, y) == self.DUNGEON_WALL:
            return False
        # Check surrounding cells
        for direction in directions.CARDINAL_DIRECTIONS:
            # Check the coordinates are in the dungeon
            if not self._dungeon_rectangle.contains(x + direction.x, y + direction.y):
                return False
            # Check the coordinates are a wall
            if not self._get_dungeon_cell(x + direction.x, y + direction.y) == self.DUNGEON_WALL:
                return False
        return True

    def print_dungeon(self):
        """A function to print the dungeon to standard out."""
        # Print Room in dungeon
        for y in range(0, self._height):
            for x in range(0, self._width):
                print(self._get_dungeon_cell(x, y), end='')
            print('')
