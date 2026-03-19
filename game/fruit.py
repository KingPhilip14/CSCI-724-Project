import random

import pygame
from pygame import Vector2

from config import cell_size, cell_number, screen, apple_img


class Fruit:
    def __init__(self):
        self.randomize()
        self.x: int = 0
        self.y: int = 0
        self.pos: Vector2 = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple_img, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
