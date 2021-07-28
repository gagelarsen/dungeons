"""An example using pygame.

This file was generated on June 03, 2020
"""
__author__ = "Gage Larsen"
__copyright__ = "Copyright: gagelarsen 2020"
__maintainer__ = "Gage Larsen"
__email__ = "gagelarsen53@gmail.com"

import pygame

from dungeons.dungeon import Dungeon
from dungeons.geometry import directions

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 64, 255)
BROWN = (165, 42, 42)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# MY CODE
dungeon_width = 35
dungeon_height = 35
dungeon = Dungeon(width=dungeon_width, height=dungeon_height, random_seed=2, has_player=True, has_enemies=True)

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = dungeon.dungeon
# grid = []
# for row in range(10):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
# grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [dungeon.width * WIDTH + MARGIN * (dungeon_width + 1),
               dungeon.height * HEIGHT + MARGIN * (dungeon_height + 1)]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Dungeon")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            dungeon = Dungeon(35, 35, has_player=True, has_enemies=True)
            grid = dungeon.dungeon
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dungeon.move_player(directions.UP)
            elif event.key == pygame.K_DOWN:
                dungeon.move_player(directions.DOWN)
            elif event.key == pygame.K_LEFT:
                dungeon.move_player(directions.LEFT)
            elif event.key == pygame.K_RIGHT:
                dungeon.move_player(directions.RIGHT)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(dungeon.height):
        for column in range(dungeon.width):
            color = BLACK
            if grid[row][column] == dungeon.DUNGEON_HALL:
                color = GREEN
            if grid[row][column] == dungeon.DUNGEON_ROOM:
                color = WHITE
            if grid[row][column] == dungeon.DUNGEON_DOORWAY:
                color = BROWN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    if dungeon.has_player:
        pygame.draw.rect(screen, BLUE,
                         [(MARGIN + WIDTH) * dungeon.player.x + MARGIN,
                          (MARGIN + HEIGHT) * dungeon.player.y + MARGIN,
                          WIDTH, HEIGHT])
    if dungeon.has_enemies:
        for enemy in dungeon.enemies:
            pygame.draw.rect(screen, RED,
                             [(MARGIN + WIDTH) * enemy.x + MARGIN,
                              (MARGIN + HEIGHT) * enemy.y + MARGIN,
                              WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
