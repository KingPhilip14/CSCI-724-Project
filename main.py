import os
import random

import config
from enums import SimMode
from game.controller import update_direction
from serialize import Serialize
from utils import is_valid_direction
from pathlib import Path

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys

import pygame
from pygame.math import Vector2

from config import SCREEN, CLOCK, FRAME_RATE, TOTAL_TRIALS
from game.engine import Engine
from visualizer.viz_logic import start_screen_loop

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    # loads the font
    font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    start_screen_loop()

    # generates a list of 3 random seeds to be used during iterations
    seeds: list[int] = [random.randint(0, 10000000) for _ in range(TOTAL_TRIALS)]

    for iteration, sim_mode in enumerate(config.sim_mode_list):
        trial_num: int = (iteration % config.TOTAL_TRIALS) + 1
        highest_mem: int = 0

        # set the random seed universally here
        seed: int = seeds[trial_num - 1]
        random.seed(seed)

        # set the config curr_mode to keep things consistent
        config.curr_mode = sim_mode

        engine = Engine(seed)

        serialize: Serialize = Serialize(sim_mode, trial_num)
        exec_times: list[float] = []
        peak_mem: int = 0

        print(f'Iteration: {iteration}\n'
              f'Simulation mode: {sim_mode}\n'
              f'Trial num: {trial_num}\n'
              f'Seed: {seed}\n\n')

        while not engine.is_game_over:
            engine.seed = seed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # to handle human input
                if event.type == pygame.KEYDOWN:
                    direction_map = {
                        pygame.K_UP: Vector2(0, -1),
                        pygame.K_RIGHT: Vector2(1, 0),
                        pygame.K_DOWN: Vector2(0, 1),
                        pygame.K_LEFT: Vector2(-1, 0),
                    }

                    if event.key in direction_map:
                        new_dir = direction_map[event.key]

                        if is_valid_direction(engine.snake.direction, new_dir):
                            engine.snake.direction = new_dir

                if sim_mode == SimMode.HUMAN:
                    if event.type == SCREEN_UPDATE:
                        engine.update()
                else:
                    # runs the given algorithm every frame to help speed it up
                    # if using an AI algorithm, get the new direction the snake would want
                    memory, exec_time = update_direction(engine, sim_mode)
                    exec_times.append(exec_time)

                    if memory > peak_mem:
                        peak_mem = memory

                    engine.update()

            SCREEN.fill((175, 215, 70))
            engine.draw_elements(trial_num, engine.snake.turns)
            pygame.display.update()

            # provides higher frame rates by multiplying by an int
            CLOCK.tick(FRAME_RATE * 5) if sim_mode is not SimMode.HUMAN else CLOCK.tick(FRAME_RATE)

            if engine.is_game_over:
                break

        avg_exec_time: float = sum(exec_times) / len(exec_times) if sim_mode != SimMode.HUMAN else 0

        serialize.serialize(engine.score, engine.snake.turns, peak_mem, avg_exec_time)

        engine.reset_snake()
        engine.is_game_over = False
