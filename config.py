import os

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
APPLE_IMG = pygame.image.load(os.path.join(os.getcwd(), 'graphics', 'apple.png')).convert_alpha()

# a list of strings based on the SimMode enums to determine
SIM_MODES: list[str] = [SimMode.BFS.name.lower(), SimMode.GBFS.name.lower(), SimMode.DIJK.name.lower(),
                         SimMode.ASTAR.name.lower(), SimMode.HUMAN.name.lower()]

# determines how many times a single algorithm should be executed; helps with getting an average for final results
TOTAL_TRIALS: int = 3

# globally used to determine what the starting Simulation Mode is
starting_mode: SimMode = SimMode.HUMAN

# globally used to determine what Simulation Mode the game is in
curr_mode: SimMode = SimMode.HUMAN

# globally used to determine all the Simulation Modes to execute
sim_mode_list: list[SimMode] = []
