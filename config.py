import os

from visualizer.button import ButtonColors

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from enums import SimMode

# the number of pixels used for a cell
CELL_SIZE: int = 40

# the number of cells to make to create the gameboard (e.g., 20x20)
CELL_NUMBER: int = 20

# the screen object used to display information to the user
SCREEN = (pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)))

# the timing feature used to determine frame rate
CLOCK = pygame.time.Clock()

# loads the apple image
APPLE_IMG = pygame.image.load('graphics/apple.png').convert_alpha()

# loads the font
FONT = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)

# a list of strings based on the SimMode enums to determine
SIM_MODES: list[str] = [SimMode.BFS.name.lower(), SimMode.GBFS.name.lower(), SimMode.DIJK.name.lower(),
                         SimMode.ASTAR.name.lower(), SimMode.HUMAN.name.lower()]

# determines how many times a single algorithm should be executed; helps with getting an average for final results
TOTAL_TRIALS: int = 3

# different colors for the buttons in the visualizer
BUTTON_COLORS: ButtonColors = ButtonColors(
        bg_color='#8C7753',             # Idle darker tan shade for the background
        bg_color_hover='#A38E68',       # Hovered slightly lighter tan
        bg_color_clicked='#735F41',     # Clicked darker brown-tan
        fg_color='#000000',             # Idle black text
        fg_color_hover='#2D2D2D',       # Hovered dark gray text
        fg_color_clicked='#494949'      # Clicked lighter gray text
    )
