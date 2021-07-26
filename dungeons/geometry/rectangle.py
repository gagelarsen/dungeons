"""The rectangle class file.

This file was generated on June 03, 2020
"""
from typing import Tuple


class Rectangle(object):
    """A class for basic rectangle functions."""
    def __init__(self, height: int, width: int, x: int = 0, y: int = 0) -> None:
        """The __init__ function for the Rectangle class."""
        self._height: int = height
        self._width: int = width
        self._x: int = x
        self._y: int = y

    @property
    def height(self) -> int:
        """The height of the rectangle."""
        return self._height

    @property
    def width(self) -> int:
        """The width of the rectangle."""
        return self._width

    @property
    def x(self) -> int:
        """The upper left corner x coordinate."""
        return self._x

    @property
    def y(self) -> int:
        """The upper left corner y coordinate."""
        return self._y

    @property
    def area(self) -> int:
        """The area of the rectangle."""
        return self._height * self._width

    @property
    def center(self) -> Tuple[int, int]:
        """The (x, y) coordinates of the center of the rectangle."""
        x = int((self.x_min + self.x_max) / 2)
        y = int((self.y_min + self.y_max) / 2)
        return x, y

    @property
    def position(self) -> Tuple[int, int]:
        """The (x, y) coordinates of the top left corner of the rectangle."""
        return self._x, self._y

    @property
    def size(self) -> Tuple[int, int]:
        """The (width, height) of the rectangle."""
        return self._width, self._height

    @property
    def x_max(self) -> int:
        """The maximum x coordinate of the rectangle."""
        return self._x + self._width

    @property
    def x_min(self) -> int:
        """The minimum x coordinate of the rectangle."""
        return self._x

    @property
    def y_max(self) -> int:
        """The maximum y coordinate of the rectangle."""
        return self._y + self._height

    @property
    def y_min(self) -> int:
        """The minimum y coordinate of the rectangle."""
        return self._y

    def contains(self, x: int, y: int) -> bool:
        """Check if the rectangle contains the point at the given x and y coordinates.

        Args:
            x (int): The x coordinate of a point
            y (int): The y coordinate of a point

        Returns:
            True if the point is contained in the rectangle, or False if it does not.
        """
        if self.x_min <= x < self.x_max:
            if self.y_min <= y < self.y_max:
                return True
        return False

    def overlaps(self, rect: 'Rectangle', can_touch: bool = False) -> bool:
        """Check if a rectangle overlaps with another rectangle.

        Args:
            rect (Rectangle): A rectangle
            can_touch (bool): Are the rectangles considered overlapping if they touch.

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

    def __eq__(self, other: 'Rectangle') -> bool:
        """The equal operator for a rectangle."""
        if type(other) is not Rectangle:
            return False
        if self is other:
            return True
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height
