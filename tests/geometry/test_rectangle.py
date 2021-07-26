"""Tests for the rectangle class in the geometry module.

This file was generated on June 03, 2020
"""
from dungeons.geometry.rectangle import Rectangle


def test_rectangle_creation_with_defaults() -> None:
    """Test creating rectangle with defaults."""
    rectangle = Rectangle(width=5, height=6)
    assert rectangle.width == 5
    assert rectangle.height == 6
    assert rectangle.x == 0
    assert rectangle.y == 0


def test_rectangle_creation() -> None:
    """Test creating rectangle with x and y set."""
    rectangle = Rectangle(width=5, height=6, x=1, y=4)
    assert rectangle.width == 5
    assert rectangle.height == 6
    assert rectangle.x == 1
    assert rectangle.y == 4


def test_rectangle_area() -> None:
    """Test getting the rectangles area."""
    rectangle = Rectangle(width=4, height=5)
    assert rectangle.area == 20  # 20 = 4 * 5


def test_rectangle_center_with_defaults() -> None:
    """Test getting the rectangles center with defaults."""
    rectangle = Rectangle(width=6, height=5)
    assert rectangle.center == (3, 2)  # ( (x1+x2)/2, (y1+y2)/2 )


def test_rectangle_center() -> None:
    """Test getting the rectangles center."""
    rectangle = Rectangle(width=4, height=7, x=5, y=7)
    assert rectangle.center == (7, 10)  # ( (x1+x2)/2, (y1+y2)/2 )


def test_rectangle_position() -> None:
    """Test getting the rectangles position."""
    rectangle = Rectangle(width=5, height=6, x=1, y=2)
    assert rectangle.position == (1, 2)  # (x, y)


def test_rectangle_size() -> None:
    """Test getting the rectangles size."""
    rectangle = Rectangle(width=6, height=4)
    assert rectangle.size == (6, 4)  # (width, height)


def test_x_max() -> None:
    """Test getting the rectangles x_max."""
    rectangle = Rectangle(width=6, height=4, x=1, y=2)
    assert rectangle.x_max == 7


def test_x_min() -> None:
    """Test getting the rectangles x_min."""
    rectangle = Rectangle(width=6, height=4, x=1, y=2)
    assert rectangle.x_min == 1


def test_y_max() -> None:
    """Test getting the rectangles y_max."""
    rectangle = Rectangle(width=6, height=4, x=1, y=2)
    assert rectangle.y_max == 6


def test_y_min() -> None:
    """Test getting the rectangles y_min."""
    rectangle = Rectangle(width=6, height=4, x=1, y=2)
    assert rectangle.y_min == 2


def test_rectangle_contains() -> None:
    """Test the rectangle can find a containing point."""
    rectangle = Rectangle(width=4, height=5, x=2, y=1)
    contains = rectangle.contains(x=3, y=3)
    assert contains is True


def test_rectangle_does_not_contains() -> None:
    """Test the rectangle can determine a point is not contained."""
    rectangle = Rectangle(width=4, height=5, x=2, y=1)
    contains = rectangle.contains(x=-4, y=3)
    assert contains is False


def test_rectangles_overlap() -> None:
    """Test the rectangle can determine if it overlaps another."""
    rectangle_1 = Rectangle(width=5, height=5, x=0, y=0)
    rectangle_2 = Rectangle(width=5, height=5, x=2, y=2)
    overlaps = rectangle_1.overlaps(rectangle_2)
    assert overlaps is True


def test_rectangles_does_not_overlap_above() -> None:
    """Test the rectangle can determine if it overlaps another."""
    rectangle_1 = Rectangle(width=10, height=10, x=0, y=0)
    rectangle_2 = Rectangle(width=5, height=5, x=2, y=-6)
    overlaps = rectangle_1.overlaps(rectangle_2)
    assert overlaps is False


def test_rectangle_overlaps_completely() -> None:
    """Test the rectangle can determine if it overlaps another completely."""
    rectangle_1 = Rectangle(width=10, height=10, x=0, y=0)
    rectangle_2 = Rectangle(width=5, height=5, x=2, y=2)
    overlaps = rectangle_1.overlaps(rectangle_2)
    assert overlaps is True


def test_rectangle_overlaps_touches() -> None:
    """Test the rectangle can detect overlaps even if just touching."""
    rectangle_1 = Rectangle(width=10, height=10, x=0, y=0)
    rectangle_2 = Rectangle(width=10, height=10, x=10, y=9)
    overlaps = rectangle_1.overlaps(rectangle_2)
    assert overlaps is True


def test_rectangle_overlaps_can_touch_right_side() -> None:
    """Test the rectangle can detect overlaps even if just touching."""
    rectangle_1 = Rectangle(width=10, height=10, x=0, y=0)
    rectangle_2 = Rectangle(width=10, height=10, x=10, y=9)
    overlaps = rectangle_1.overlaps(rectangle_2, can_touch=True)
    assert overlaps is False


def test_rectangle_overlaps_can_touch_below() -> None:
    """Test the rectangle can detect overlaps even if just touching."""
    rectangle_1 = Rectangle(width=10, height=10, x=0, y=0)
    rectangle_2 = Rectangle(width=10, height=10, x=9, y=10)
    overlaps = rectangle_1.overlaps(rectangle_2, can_touch=True)
    assert overlaps is False


def test_rectangles_does_not_overlap() -> None:
    """Test the rectangle can detect it does not overlap."""
    rectangle_1 = Rectangle(width=5, height=5, x=0, y=0)
    rectangle_2 = Rectangle(width=5, height=5, x=10, y=9)
    overlaps = rectangle_1.overlaps(rectangle_2)
    assert overlaps is False


def test_rectangles_equal() -> None:
    """Test two rectangles are equal."""
    rectangle_1 = Rectangle(width=5, height=5, x=0, y=0)
    rectangle_2 = Rectangle(width=5, height=5, x=0, y=0)
    assert rectangle_1 == rectangle_2


def test_rectangles_not_equal() -> None:
    """Test two rectangles are not equal."""
    rectangle_1 = Rectangle(width=5, height=5, x=0, y=0)
    rectangle_2 = Rectangle(width=5, height=6, x=0, y=0)
    assert not rectangle_1 == rectangle_2


def test_rectangles_same() -> None:
    """Test two rectangles are equal if they are the same."""
    rectangle_1 = Rectangle(width=5, height=5, x=0, y=0)
    assert rectangle_1 == rectangle_1


def test_rectangles_not_equal_different_type() -> None:
    """Test rectangle doesn't match different type."""
    rectangle_1 = Rectangle(width=5, height=5, x=0, y=0)
    assert not rectangle_1 == 1
