"""The dungeon class file.

This file was generated on June 03, 2020
"""
import random
from typing import List

from dungeons.geometry import directions
from dungeons.geometry.rectangle import Rectangle
from dungeons.pieces import Enemy, Player


class Dungeon(object):
    """A class to contain all the information about a dungeon that will be generated."""

    DUNGEON_ROOM = ' '
    DUNGEON_HALL = '*'
    DUNGEON_WALL = 'X'
    DUNGEON_DOORWAY = '$'
    PLAYER_PIECE = 'P'
    ENEMY_PIECE = 'E'

    def __init__(self, width: int, height: int, random_seed: int = None, room_attempts: int = 100,
                 max_room_width: int = 10, max_room_height: int = 10, min_room_width: int = 5,
                 min_room_height: int = 5, randomness: float = 0.5, has_player: bool = False,
                 has_enemies: bool = False) -> None:
        """__init__ function for the Dungeon class.

        Args:
            width (int): Width of the dungeon.
            height (int): Height of the dungeon.
            random_seed (int): Seed for the dungeon.
            room_attempts (int): Number of attempts to make rooms.
            max_room_width (int): Max room width.
            max_room_height (int): Max room height.
            min_room_width (int): Minimum room width.
            min_room_height (int): Minimum room height.
            randomness (float): Percentage of randomness 0 to 100.
            has_player (bool): Is there a player in this dungeon.
            has_enemies (bool): Are there enemies in this dungeon.
        """
        self._width = width
        self._height = height
        self._room_attempts = room_attempts
        self._max_room_width = max_room_width
        self._min_room_width = min_room_width
        self._max_room_height = max_room_height
        self._min_room_height = min_room_height
        self.dungeon = []  # This is in the form dungeon[y][x]

        self._randomness = randomness

        self._dungeon_rectangle = Rectangle(width=self._width, height=self._height)
        self._rooms = []

        self._has_player = has_player
        self._has_enemies = has_enemies

        if random_seed is not None:
            random.seed(random_seed)

        # Fill the Dungeon Array
        for _ in range(self._height):
            row = [self.DUNGEON_WALL for _ in range(self._width)]
            self.dungeon.append(row)

        # Add Rooms
        self._generate_rooms()

        # Add Passages
        self._carve_passages()
        self._open_rooms()

        # Remove Dead Ends
        self._remove_dead_ends()

        self._player = None
        self._player_room_number = None
        if self.has_player:
            self._add_player()

        self._enemies = []
        if self.has_enemies:
            self._generate_enemies()

    @property
    def width(self) -> int:
        """The width of the dungeon."""
        return self._width

    @property
    def height(self) -> int:
        """The height of the dungeon."""
        return self._height

    @property
    def randomness(self) -> float:
        """The randomness of the dungeon passages."""
        if self._randomness > 1:
            return 1
        if self._randomness < 0:
            return 0
        return self._randomness

    @property
    def has_player(self) -> bool:
        """Does this dungeon have a player object."""
        return self._has_player

    @property
    def player(self) -> Player:
        """This dungeons player object."""
        return self._player

    @property
    def has_enemies(self) -> bool:
        """Does this dungeon have enemies."""
        return self._has_enemies

    @property
    def enemies(self) -> List[Enemy]:
        """Dungeon enemies."""
        return self._enemies

    def _set_dungeon_cell(self, x: int, y: int, value: str) -> None:
        """Set the value of a specified dungeon cell.

        Args:
            x (int): The specified x coordinate.
            y (int): The specified y coordinate.
            value (str): The new value of the cell.
        """
        self.dungeon[y][x] = value

    def _get_dungeon_cell(self, x: int, y: int) -> str:
        """Get the value of a specified dungeon cell.

        Args:
            x (int): The x location of the dungeon.
            y (int): The y location of the dungeon.

        Returns:
            str: The string value at the x, y location.
        """
        return self.dungeon[y][x]

    def _generate_rooms(self) -> None:
        """Generate random rooms."""
        for _ in range(self._room_attempts):
            # Get Random Dimensions for New Room
            x = random.randint(1, self._width - 1)
            y = random.randint(1, self._height - 1)
            room_width = random.randint(self._min_room_width, self._max_room_width)
            room_height = random.randint(self._min_room_height, self._max_room_height)
            new_room = Rectangle(width=room_width, height=room_height, x=x, y=y)

            # Make sure the room doesn't overlap other rooms
            overlaps = False
            for room in self._rooms:
                if room.overlaps(new_room):
                    overlaps = True
                    break

            in_dungeon = False
            if not (not self._dungeon_rectangle.contains(new_room.x, new_room.y) or not
                    self._dungeon_rectangle.contains(new_room.x_max, new_room.y_max)):
                in_dungeon = True
            if not overlaps and in_dungeon:
                self._rooms.append(new_room)
        # Add Rooms to Dungeons
        for room in self._rooms:
            for x in range(room.x, room.x + room.width):
                for y in range(room.y, room.y + room.height):
                    self._set_dungeon_cell(x, y, self.DUNGEON_ROOM)

    def _carve_passages(self) -> None:
        """Carve passages in the maze."""
        # Loop through the dungeon to create maze.
        for y in range(1, self._height):
            for x in range(1, self._width):
                self._carve_passage_helper(x, y)

    def _carve_passage_helper(self, start_x: int, start_y: int, last_direction: directions.Direction = None) -> None:
        """Carving the dungeon passages helper function.

        Args:
            start_x (int): the starting x coordinate for the passageway.
            start_y (int): the starting y coordinate for the passageway.
            last_direction (directions.Direction): the last direction a passage was carved.
        """
        # Check if the cell can be carved
        if not self._can_carve_passage(start_x, start_y, last_direction):
            return

        # Carve the current cell
        self._set_dungeon_cell(start_x, start_y, self.DUNGEON_HALL)

        available_directions = [direction for direction in directions.DPAD_DIRECTIONS
                                if self._can_carve_passage(start_x + direction.x, start_y + direction.y, direction)]
        # Pick a new direction
        while len(available_directions) > 0:
            change_direction = random.random() < self._randomness
            if last_direction not in available_directions:
                change_direction = True

            new_direction = last_direction
            if change_direction or new_direction is None:
                new_direction_index = random.randint(0, len(available_directions) - 1)
                new_direction = available_directions[new_direction_index]
            available_directions.remove(new_direction)
            self._carve_passage_helper(start_x + new_direction.x, start_y + new_direction.y, new_direction)

    def _can_carve_passage(self, x: int, y: int, incoming_direction: directions.Direction = None) -> bool:
        """Determine if a passage can be carved at a specified location in the dungeon.

        Args:
            x (int): the x coordinate of the cell to check
            y (int): the y coordinate of the cell to check
            incoming_direction (directions.Direction): The direction that the passage has been moving.

        Returns:
            True if the cell can be carved, or false if it cannot.
        """
        # Make sure the section is a wall
        if not self._get_dungeon_cell(x, y) == self.DUNGEON_WALL:
            return False
        # Check surrounding cells
        for direction in directions.CARDINAL_DIRECTIONS:
            # Check the coordinates are in the dungeon
            if not self._dungeon_rectangle.contains(x + direction.x, y + direction.y):
                return False
            # We can ignore cells behind us.
            if incoming_direction is not None:
                if incoming_direction.y == directions.UP.y or incoming_direction.y == directions.DOWN.y:
                    if incoming_direction.y * -1 == direction.y:
                        continue
                if incoming_direction.x == directions.LEFT.x or incoming_direction.x == directions.RIGHT.x:
                    if incoming_direction.x * -1 == direction.x:
                        continue
            # Check the coordinates are a wall
            if not self._get_dungeon_cell(x + direction.x, y + direction.y) == self.DUNGEON_WALL:
                return False
        return True

    def _open_rooms(self) -> None:
        """Open the rooms to the passageways."""
        # Loop Through Rooms
        for room in self._rooms:
            possible_directions = [x for x in directions.DPAD_DIRECTIONS]
            multiple_openings = random.random() > 0.75
            has_opening = False
            while len(possible_directions) > 0:
                direction = possible_directions[random.randint(0, len(possible_directions) - 1)]
                possible_directions.remove(direction)

                possible_locations = []
                if direction == directions.UP:
                    possible_locations = [(x, room.y_min - 1)
                                          for x in range(room.x_min, room.x_max)]
                elif direction == directions.DOWN:
                    possible_locations = [(x, room.y_max)
                                          for x in range(room.x_min, room.x_max)]
                elif direction == directions.LEFT:
                    possible_locations = [(room.x_min - 1, y)
                                          for y in range(room.y_min, room.y_max)]
                elif direction == directions.RIGHT:
                    possible_locations = [(room.x_max, y)
                                          for y in range(room.y_min, room.y_max)]

                # Loop through random locations till you find one that can be opened.
                while len(possible_locations) > 0:
                    location = possible_locations[random.randint(0, len(possible_locations) - 1)]
                    possible_locations.remove(location)
                    if self._can_carve_entry(location[0], location[1], direction):
                        self._set_dungeon_cell(location[0], location[1], self.DUNGEON_DOORWAY)
                        has_opening = True
                        break

                # Break if done
                if has_opening and not multiple_openings:
                    break

    def _can_carve_entry(self, x: int, y: int, incoming_direction: directions.Direction) -> bool:
        """Check if an entry can be carved.

        Args:
            x (int): The x location to check.
            y (int): The y location to check.
            incoming_direction (directions.Direction): The incoming direction.

        Returns:
            bool: If an entry can be carved.
        """
        # Is the cell I am trying to change a wall
        if self._get_dungeon_cell(x, y) != self.DUNGEON_WALL:
            return False

        # Is the next cell in the rectangle
        if not self._dungeon_rectangle.contains(x + incoming_direction.x, y + incoming_direction.y):
            return False

        # Does the room I am trying to change connect to a room or hall?
        if not self._get_dungeon_cell(x + incoming_direction.x, y + incoming_direction.y) == self.DUNGEON_HALL and \
                not self._get_dungeon_cell(x + incoming_direction.x, y + incoming_direction.y) == self.DUNGEON_ROOM:
            return False

        if incoming_direction == directions.UP or incoming_direction == directions.DOWN:
            if not self._get_dungeon_cell(x - 1, y) == self.DUNGEON_WALL or \
                    not self._get_dungeon_cell(x + 1, y) == self.DUNGEON_WALL:
                return False
        if incoming_direction == directions.LEFT or incoming_direction == directions.RIGHT:
            if not self._get_dungeon_cell(x, y - 1) == self.DUNGEON_WALL or \
                    not self._get_dungeon_cell(x, y + 1) == self.DUNGEON_WALL:
                return False
        return True

    def _remove_dead_ends(self) -> None:
        """Remove maze dead ends."""
        for y in range(0, self._height):
            for x in range(0, self._width):
                self._remove_dead_ends_helper(x, y)

    def _remove_dead_ends_helper(self, x: int, y: int) -> None:
        """Remove dead ends helper fuction.

        Args:
            x: x location to remove dead ends.
            y: y location to remove dead ends.
        """
        cell = self._get_dungeon_cell(x, y)
        if cell == self.DUNGEON_HALL:
            d_pad_directions = [x for x in directions.DPAD_DIRECTIONS]
            connections = []
            for direction in d_pad_directions:
                connected_cell = self._get_dungeon_cell(x + direction.x, y + direction.y)
                if connected_cell in [self.DUNGEON_HALL, self.DUNGEON_DOORWAY, self.DUNGEON_ROOM]:
                    connections.append((x + direction.x, y + direction.y))
            if len(connections) <= 1:
                self._set_dungeon_cell(x, y, self.DUNGEON_WALL)
                if len(connections) == 1:
                    self._remove_dead_ends_helper(connections[0][0], connections[0][1])

    def print_dungeon(self) -> None:
        """Print the dungeon to standard out."""
        # Print Room in dungeon
        for y in range(0, self._height):
            for x in range(0, self._width):
                print(self._get_dungeon_cell(x, y), end='')
            print('')

    def _add_player(self) -> None:
        """Add a player to the dungeon."""
        self._player_room_number = random.randint(0, len(self._rooms) - 1)
        room = self._rooms[self._player_room_number]
        self._player = Player(x=room.x, y=room.y, name='main_player')

    def _player_can_move(self, direction: directions.Direction) -> bool:
        """Can the player move in a specified direction.

        Args:
            direction (directions.Direction): Direction the player wants to move.

        Returns:
            True if the player can move, False otherwise.
        """
        destination_x = self.player.x + direction.x
        destination_y = self.player.y + direction.y
        destination = self._get_dungeon_cell(destination_x, destination_y)

        if destination in [self.DUNGEON_WALL]:
            return False
        return True

    def move_player(self, direction: directions.Direction) -> None:
        """Move the dungeon players position.

        Args:
            direction (direction.Direction): The direction to move the player.
        """
        if self._player_can_move(direction):
            self.player.move(direction)

    def _generate_enemies(self) -> None:
        """Generate enemies in the dungeon."""
        for room in self._rooms:
            if self.has_player and room is self._rooms[self._player_room_number]:
                continue
            number_of_enemies = random.randint(1, 3)
            for _ in range(number_of_enemies):
                enemy = Enemy(
                    x=random.randint(room.x_min, room.x_max - 1),
                    y=random.randint(room.y_min, room.y_max - 1),
                    threat_level=random.randint(0, 10),
                )
                self._enemies.append(enemy)
