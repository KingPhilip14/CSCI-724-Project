import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys

import pygame
from pygame.math import Vector2

from config import SCREEN, CLOCK
from game.engine import Engine

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    engine = Engine()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                engine.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if engine.snake.direction.y != 1:
                        engine.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT:
                    if engine.snake.direction.x != -1:
                        engine.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if engine.snake.direction.y != -1:
                        engine.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if engine.snake.direction.x != 1:
                        engine.snake.direction = Vector2(-1, 0)

        SCREEN.fill((175, 215, 70))
        engine.draw_elements()
        pygame.display.update()

        # provides 60 FPS (or the best it can)
        CLOCK.tick(60)
