"""The dungeon class file.

This file was generated on June 03, 2020
"""
__author__ = "Gage Larsen"
__copyright__ = "Copyright: (c) Aquaveo 2020"
__maintainer__ = "Gage Larsen"
__email__ = "gagelarsen53@gmail.com"

import random

from dungeons.geometry.rectangle import Rectangle


class Dungeon(object):
    """A class to contain all the information about a dungeon that will be generated."""
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

        self._dungeon_rectangle = Rectangle(width=self._width, height=self._height)
        self.rooms = []

        if random_seed is not None:
            random.seed(random_seed)

        self._generate_rooms()
        x = 0

    @property
    def width(self):
        """The width of the dungeon."""
        return self._width

    @property
    def height(self):
        """The height of the dungeon."""
        return self._height

    def _generate_rooms(self):
        for _ in range(self._room_attempts):
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
            if not (not self._dungeon_rectangle.contains(new_room.x, new_room.y)
                    or not self._dungeon_rectangle.contains(new_room.x_max, new_room.y_max)):
                in_dungeon = True
            if not overlaps and in_dungeon:
                self.rooms.append(new_room)

    def print_dungeon(self):
        ROOM = ' '
        WALL = 'X'

        # Create Dungeon Base
        dungeon = []
        for x in range(self._height):
            row = [WALL for _ in range(self._width)]
            dungeon.append(row)

        # Add Rooms
        for room in self.rooms:
            for x in range(room.x, room.x + room.width):
                for y in range(room.y, room.y + room.height):
                    dungeon[y][x] = ROOM

        # Print Room in dungeon
        for y in dungeon:
            for x in y:
                print(x, end='')
            print('')

