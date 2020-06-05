# Dungeons

This is a library that uses procedural generation to create a dungeon with a maze of passageways connecting the rooms

![](https://github.com/gagelarsen/dungeons/workflows/Main-CI/badge.svg)

## Minor Example
```python
from dungeons.dungeon import Dungeon

d1 = Dungeon(100, 50)
d1.print_dungeon()
```
This example will create you a random dungeon that is 100 squares wide, and 50 squares tall. The indexing is 0,0 based starting at the top left corner.

There are several kwargs for the dungeon class you can use for adjusting settings of your dungeon:

**random_seed:** This sets the seed so you can generate the same dungeon for testing purposes.<br>
**randomness:** This sets the randomness variability for the maze hallways.<br>
**room_attempts:** This sets the number of attempts it will try to make randomly sized and placed rooms.<br>
**max_room_width:** The max possible width of rooms in the dungeon.<br>
**min_room_width:** The min possible width of rooms in the dungeon.<br>
**max_room_height:** The max possible height of rooms in the dungeon.<br>
**min_room_height:** The min possible height of rooms in the dungeon.<br>