import os
import random

import config
from enums import SimMode
from game.controller import update_direction
from serialize import Serialize

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys

import pygame
from pygame.math import Vector2

from config import SCREEN, CLOCK, FRAME_RATE
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
    seeds: list[int] = [random.randint(0, 10000000), random.randint(0, 10000000), random.randint(0, 10000000)]

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

                # # for when the screen updates
                # if event.type == SCREEN_UPDATE:
                #     if sim_mode != SimMode.HUMAN:
                #         # if using an AI algorithm, get the new direction the snake would want
                #         memory, exec_time = update_direction(engine, sim_mode)
                #         exec_times.append(exec_time)
                #
                #         if memory > peak_mem:
                #             peak_mem = memory
                #
                #     engine.update()

            SCREEN.fill((175, 215, 70))
            engine.draw_elements(trial_num, engine.snake.turns)
            pygame.display.update()

            # provides 60 FPS (or the best it can)
            CLOCK.tick(FRAME_RATE) if sim_mode is not SimMode.HUMAN else CLOCK.tick(FRAME_RATE * 5)

            if engine.is_game_over:
                break

        avg_exec_time: float = sum(exec_times) / len(exec_times) if sim_mode != SimMode.HUMAN else 0

        serialize.serialize(engine.score, engine.snake.turns, peak_mem, avg_exec_time)

        engine.reset_snake()
        engine.is_game_over = False
