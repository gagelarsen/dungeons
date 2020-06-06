"""Tests for the generate functionality of the dungeons package."""
from dungeons.dungeon import Dungeon


def test_dungeon():
    """A test to check the base initialization of a dungeon."""
    dungeon = Dungeon(width=10, height=20)
    assert dungeon.width == 10
    assert dungeon.height == 20
    assert dungeon.randomness == 0.5


def test_dungeon_randomness_max():
    """A test to check the max of a dungeons randomness."""
    dungeon = Dungeon(width=10, height=20, randomness=10)
    assert dungeon.randomness == 1


def test_dungeon_randomness_min():
    """A test to check the min of a dungeons randomness."""
    dungeon = Dungeon(width=10, height=20, randomness=-4)
    assert dungeon.randomness == 0


def test_print_dungeon(capsys):
    """A test to check the printing of the dungeon."""
    dungeon = Dungeon(width=20, height=10, random_seed=2)
    dungeon.print_dungeon()
    captured = capsys.readouterr()

    expected = \
        'XXXXXXXXXXXXXXXXXXXX\n' \
        'XXXXXXXXXXXXXXXXXXXX\n' \
        'XX     X     X     X\n' \
        'XX     X     $     X\n' \
        'XX     X     X     X\n' \
        'XX     X     X     X\n' \
        'XX     $     $     X\n' \
        'XX     XXXXXXX     X\n' \
        'XX     X*****X     X\n' \
        'XXXXXXXXXXXXXXXXXXXX\n'

    assert captured.out == expected


def test_can_open_room_cell_is_not_a_wall():
    """Test you can't open a door outside of the dungeon."""
    dungeon = Dungeon(width=20, height=10, random_seed=2)
    can_carve = dungeon._can_carve_entry(2, 2, None)
    assert can_carve is False
