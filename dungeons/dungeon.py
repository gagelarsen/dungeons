"""The dungeon class file.

This file was generated on June 03, 2020
"""
__author__ = "Gage Larsen"
__copyright__ = "Copyright: (c) Aquaveo 2020"
__maintainer__ = "Gage Larsen"
__email__ = "gagelarsen53@gmail.com"


class Dungeon(object):
    """A class to contain all the information about a dungeon that will be generated."""
    def __init__(self, width, height):
        """The __init__ function for the Dungeon class."""
        self._width = width
        self._height = height

    @property
    def width(self):
        """The width of the dungeon."""
        return self._width

    @property
    def height(self):
        """The height of the dungeon."""
        return self._height
