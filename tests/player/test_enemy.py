"""
Tests for the enemy class.

This file was created on July 27, 2021
"""
from dungeons.geometry import directions
from dungeons.player import Enemy


def test_basic_enemy() -> None:
    """Test basic enemy."""
    enemy = Enemy(x=56, y=99, name='test_enemy')
    assert enemy.x == 56
    assert enemy.y == 99
    assert enemy.name == 'test_enemy'


def test_move_enemy() -> None:
    """Test moving the enemy."""
    enemy = Enemy(x=50, y=50, name='moving_enemy')

    enemy.move_enemy(directions.UP)
    assert enemy.x == 50
    assert enemy.y == 49

    enemy.move_enemy(directions.LEFT)
    assert enemy.x == 49
    assert enemy.y == 49

    enemy.move_enemy(directions.DOWN)
    assert enemy.x == 49
    assert enemy.y == 50

    enemy.move_enemy(directions.RIGHT)
    assert enemy.x == 50
    assert enemy.y == 50
