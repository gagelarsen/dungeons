"""
Tests for the player class.

This file was created on July 27, 2021
"""
from dungeons.geometry import directions
from dungeons.pieces import Player


def test_basic_player() -> None:
    """Test basic player."""
    player = Player(x=56, y=99, name='test_player')
    assert player.x == 56
    assert player.y == 99
    assert player.name == 'test_player'


def test_move_player() -> None:
    """Test moving the player."""
    player = Player(x=50, y=50, name='moving_player')

    player.move_player(directions.UP)
    assert player.x == 50
    assert player.y == 49

    player.move_player(directions.LEFT)
    assert player.x == 49
    assert player.y == 49

    player.move_player(directions.DOWN)
    assert player.x == 49
    assert player.y == 50

    player.move_player(directions.RIGHT)
    assert player.x == 50
    assert player.y == 50
