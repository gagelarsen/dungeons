"""Tests for the generate functionality of the dungeons package."""
from dungeons.dungeon import Dungeon


def test_dungeon():
    """A test to check the base initialization of a dungeon."""
    dungeon = Dungeon(width=10, height=20)
    assert dungeon.width == 10
    assert dungeon.height == 20
