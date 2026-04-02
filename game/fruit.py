import random

import pygame
from pygame import Vector2

from config import CELL_SIZE, CELL_NUMBER, SCREEN, APPLE_IMG


class Fruit:
    def __init__(self):
        self.randomize()
        self.x: int = 0
        self.y: int = 0
        self.pos: Vector2 = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        SCREEN.blit(APPLE_IMG, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
