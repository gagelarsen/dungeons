"""Tests for the generate functionality of the dungeons package."""
from dungeons.dungeon import Dungeon


def test_dungeon():
    """A test to check the base initialization of a dungeon."""
    dungeon = Dungeon(width=10, height=20)
    assert dungeon.width == 10
    assert dungeon.height == 20


def test_print_dungeon(capsys):
    """A test to check the printing of the dungeon."""
    dungeon = Dungeon(width=20, height=10, random_seed=2)
    dungeon.print_dungeon()
    captured = capsys.readouterr()

    expected = \
        'XXXXXXXXXXXXXXXXXXXX\n' \
        'XXXXXXXXXXXXXXXXXXXX\n' \
        'XX     X     X     X\n' \
        'XX     X     X     X\n' \
        'XX     X     X     X\n' \
        'XX     X     X     X\n' \
        'XX     X     X     X\n' \
        'XX     XXXXXXX     X\n' \
        'XX     XXXXXXX     X\n' \
        'XXXXXXXXXXXXXXXXXXXX\n'

    assert captured.out == expected
