import pygame

# the number of pixels used for a cell
cell_size: int = 40

# the number of cells to make to create the gameboard (e.g., 20x20)
cell_number: int = 20

# the screen object used to display information to the user
screen = (pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)))

# the timing feature used to determine frame rate
clock = pygame.time.Clock()

# loads the apple image
apple_img = pygame.image.load('Graphics/apple.png').convert_alpha()
