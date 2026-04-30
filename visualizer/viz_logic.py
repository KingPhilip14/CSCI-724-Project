import sys
import pygame

from config import SCREEN
from visualizer.adapter import Adapter


def start_screen_loop() -> None:
    in_loop: bool = True
    adapter: Adapter = Adapter(SCREEN)

    while in_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    in_loop = False

            if in_loop:
                in_loop = adapter.start_menu_event(event)

        adapter.start_menu_render()
        pygame.display.flip()
