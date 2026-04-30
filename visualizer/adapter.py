from visualizer.menu_template import *

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from typing import Any
from pygame import Vector2
from visualizer.text import Text


class Adapter:
    """
    The Adapter class can be considered the "Master Controller" of the Visualizer; it works in tandem with main.py.
    Main.py will call many of the methods that are provided in here to keep the Visualizer moving smoothly.
    """

    def __init__(self, screen):
        self.screen: pygame.Surface = screen
        self.populate_bytesprite: pygame.sprite.Group = pygame.sprite.Group()

        # different colors for the buttons in the visualizer
        self.button_colors: ButtonColors = ButtonColors(
            bg_color='#76944C',  # Idle green shade for the background
            bg_color_hover='#94B565',  # Hovered slightly lighter green
            bg_color_clicked='#526b2e',  # Clicked darker green background
            fg_color='#FFD21F',  # Idle yellow text
            fg_color_hover='#FFDE5C',  # Hovered lighter yellow text
            fg_color_clicked='#FFFFFF'  # Clicked white text
        )

        self.menu: BasicMenu = BasicMenu(screen, pygame.font.Font('font/PoetsenOne-Regular.ttf', 25), '#76944C', self.button_colors,
                                        'A Comparative Analysis: Snake')
        self.turn_number: int = 0
        # self.turn_max: int = MAX_TICKS

    # Define any methods button may run

    def start_menu_event(self, event: pygame.event) -> Any:
        """
        This method is used to manage any events that will occur on the starting screen. For example, a start button
        is implemented currently. Pressing it or pressing enter will start the visualizer to show the game's results.
        This method will manage any specified events and return them (hence why the return type is Any). Refer to
        menu_templates.py's start_events method for more info.
        :param event: The pygame event triggered each frame. See
        `pygame <https://www.pygame.org/docs/ref/event.html for more information>`_
        for more information.
        :return: Any specified event desired in the start_events method
        """
        return self.menu.start_events(event)

    def start_menu_render(self) -> None:
        """
        Renders and shows everything in the start menu.
        :return: None
        """
        self.menu.title.render()
        self.menu.render_buttons()

    def recalc_animation(self, turn_log: dict) -> None:
        """
        This method is called every time the turn changes
        :param turn_log: A dictionary containing the entire turn state
        :return: None
        """
        self.turn_number = turn_log['tick']

    def render(self) -> None:
        """
        This method contains all logic for rendering additional text, buttons, and other visuals
        during the playback phase.
        :return: None
        """
        text = Text(self.screen, f'{self.turn_number} / {self.turn_max}', 48)
        text.rect.center = vector_as_tuple(
            Vector2(*self.screen.get_rect().midtop))  # Vector(*self.screen.get_rect().midtop).add_y(50).as_tuple()
        # text.rect.center = Vector(*self.screen.get_rect().midtop).add_y(50).as_tuple()
        text.render()
