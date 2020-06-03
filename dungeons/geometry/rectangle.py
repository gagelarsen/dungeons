"""The rectangle class file.

This file was generated on June 03, 2020
"""
__author__ = "Gage Larsen"
__copyright__ = "Copyright: (c) Aquaveo 2020"
__maintainer__ = "Gage Larsen"
__email__ = "gagelarsen53@gmail.com"


class Rectangle(object):
    """A class for basic rectangle functions."""
    def __init__(self, height, width, x=0, y=0):
        """The __init__ function for the Rectangle class."""
        self._height = height
        self._width = width
        self._x = x
        self._y = y

    @property
    def height(self):
        """The height of the rectangle."""
        return self._height

    @property
    def width(self):
        """The width of the rectangle."""
        return self._width

    @property
    def x(self):
        """The upper left corner x coordinate."""
        return self._x

    @property
    def y(self):
        """The upper left corner y coordinate."""
        return self._y

    @property
    def area(self):
        """The area of the rectangle."""
        return self._height * self._width

    @property
    def center(self):
        """The (x, y) coordinates of the center of the rectangle."""
        x = (self.x_min + self.x_max) / 2
        y = (self.y_min + self.y_max) / 2
        return x, y

    @property
    def position(self):
        """The (x, y) coordinates of the top left corner of the rectangle."""
        return self._x, self._y

    @property
    def size(self):
        """The (width, height) of the rectangle."""
        return self._width, self._height

    @property
    def x_max(self):
        """The maximum x coordinate of the rectangle."""
        return self._x + self._width

    @property
    def x_min(self):
        """The minimum x coordinate of the rectangle."""
        return self._x

    @property
    def y_max(self):
        """The maximum y coordinate of the rectangle."""
        return self._y + self._height

    @property
    def y_min(self):
        """The minimum y coordinate of the rectangle."""
        return self._y

    def contains(self, x, y):
        """Check if the rectangle contains the point at the given x and y coordinates.

        Args:
            x: The x coordinate of a point
            y: The y coordinate of a point

        Returns:
            True if the point is contained in the rectangle, or False if it does not.
        """
        if self.x_min < x < self.x_max:
            if self.y_min < y < self.y_max:
                return True
        return False

    def overlaps(self, rect, can_touch=False):
        """Check if a rectangle overlaps with another rectangle.

        Args:
            rect: A rectangle

        Returns:
            True if the given rectangle overlaps or touches this rectangle, or False if it does not.
        """
        if can_touch:
            # If one rectangle is on the left side of other
            if self.x_min >= rect.x_max or self.x_max <= rect.x_min:
                return False

            # If one rectangle is above other
            if self.y_min >= rect.y_max or self.y_max <= rect.y_min:
                return False
        else:
            # If one rectangle is on the left side of other
            if self.x_min > rect.x_max or self.x_max < rect.x_min:
                return False

            # If one rectangle is above other
            if self.y_min > rect.y_max or self.y_max < rect.y_min:
                return False

        return True
