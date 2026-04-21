import os

# from visualizer.config import VizConfig

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from config import CELL_SIZE, CELL_NUMBER, SCREEN, APPLE_IMG
import config
from game.fruit import Fruit
from game.snake import Snake
from search.bfs import BFSPathfinder
from search.dijkstra import DijkstraPathfinder


class Engine:
    def __init__(self):
        # self.viz_config = VizConfig()
        self.snake = Snake()
        self.fruit = Fruit()
        self.font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)
        # initialize the pathfinder BFS
        # self.pathfinder = BFSPathfinder(cell_number)
        # initialize Dijkstra pathfinder
        # self.pathfinder = DijkstraPathfinder(cell_number)

    def update(self):
        # create the next move
        # next_move = self.pathfinder.find_next_move(
        #     self.snake.body[0],
        #     self.fruit.pos,
        #     self.snake.body,
        #     self.snake.direction
        # )
        # self.snake.direction = next_move
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
        
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(SCREEN, grass_color, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(SCREEN, grass_color, grass_rect)

    def draw_score(self):
        score_text: str = str(len(self.snake.body) - 3)
        curr_mode_text: str = config.curr_mode.name

        # loads the font
        game_font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = APPLE_IMG.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)

        curr_mode_surface = self.font.render(curr_mode_text, True, (56, 74, 12))
        curr_mode_x = int(CELL_SIZE * CELL_NUMBER * 0.075)
        curr_mode_y = int(CELL_SIZE * CELL_NUMBER * 0.1)
        curr_mode_rect = curr_mode_surface.get_rect(center=(curr_mode_x, curr_mode_y))
        mode_bg_rect = pygame.Rect(curr_mode_rect.left, curr_mode_rect.top, curr_mode_rect.width + 15,
                              curr_mode_rect.height)

        pygame.draw.rect(SCREEN, (167, 209, 61), bg_rect)
        SCREEN.blit(score_surface, score_rect)
        SCREEN.blit(APPLE_IMG, apple_rect)
        pygame.draw.rect(SCREEN, (56, 74, 12), bg_rect, 2)

        SCREEN.blit(curr_mode_surface, curr_mode_rect)
        pygame.draw.rect(SCREEN, (167, 209, 61), mode_bg_rect, 2)
