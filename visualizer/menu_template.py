import os

from pygame.font import Font

from enums import SimMode

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from typing import Any
from pygame import Vector2
from visualizer.button import Button, ButtonColors
from visualizer.text import Text
from utils import add_vectors, vector_as_tuple

"""
This is file is for creating different templates for the start menu of the visualizer. Each different menu screen 
will be a different class. The Basic class is the default template for the screen. Create extra classes for 
different start menu screens. The Basic class can be used as a template on how to do so.
"""


class MenuTemplate:
    """
    Menu Template is used as an interface. It provides a screen object from pygame.Surface, a 'Start Game' and
    'Exit' button. These are common attributes to all menus, so they are provided to facilitate creating them. Any
    other buttons should be created.

    This class also provides methods that are expanded upon in the Basic class, which is also in this file. Refer to
    that class' documentation for further detail. These provided methods can be used via inheritance and expanded upon
    as needed.

    NOTE: The provided buttons are already made to be in the center of the screen.
    """

    def __init__(self, screen: pygame.Surface, font: Font, text_color: str, button_colors: ButtonColors):
        self.screen: pygame.Surface = screen
        self.font = font
        self.text_color = text_color
        self.button_colors = button_colors

        self.a_star_btn: Button = Button(screen, 'A*', lambda: False, font_size=24, padding=10,
                                         colors=self.button_colors, sim_mode=SimMode.ASTAR)
        self.bfs_btn: Button = Button(screen, 'BFS', lambda: False, font_size=24, padding=10,
                                      colors=self.button_colors, sim_mode=SimMode.BFS)
        self.dijk_btn: Button = Button(screen, 'Dijkstra\'s', lambda: False, font_size=24, padding=10,
                                       colors=self.button_colors, sim_mode=SimMode.DIJK)
        self.gbfs_btn: Button = Button(screen, 'GBFS', lambda: False, font_size=24, padding=10,
                                       colors=self.button_colors, sim_mode=SimMode.GBFS)
        self.human_btn: Button = Button(screen, 'Human', lambda: False, font_size=24, padding=10,
                                        colors=self.button_colors, sim_mode=SimMode.HUMAN)
        # self.all_btn: Button = Button(screen, 'All', lambda: False, font_size=24, padding=10,
        #                               colors=self.button_colors, sim_mode=SimMode.ALL)

        # The next two variables shouldn't be type hinted. The center is a tuple of two ints (i.e., tuple[int, int])
        self.a_star_btn.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
                                                                  Vector2(-300, -60)))
        self.bfs_btn.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
                                                               Vector2(0, -60)))
        self.dijk_btn.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
                                                                Vector2(300, -60)))
        self.gbfs_btn.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
                                                                Vector2(-300, 110)))
        # self.all_btn.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
        #                                                        Vector2(0, 110)))
        self.human_btn.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
                                                                 Vector2(300, 110)))

    def start_events(self, event: pygame.event) -> Any:
        """
        This method will return if the user presses the 'Start Game' button. The return type is Any since that's what
        the `mouse_clicked()` method returns.
        :param event:
        :return: Any
        """
        return self.a_star_btn.mouse_clicked(event) if self.a_star_btn.mouse_clicked(event) is not None else \
            self.bfs_btn.mouse_clicked(event) if self.bfs_btn.mouse_clicked(event) is not None else \
                self.dijk_btn.mouse_clicked(event) if self.dijk_btn.mouse_clicked(event) is not None else \
                    self.gbfs_btn.mouse_clicked(event) if self.gbfs_btn.mouse_clicked(event) is not None else \
                        self.human_btn.mouse_clicked(event) if self.human_btn.mouse_clicked(event) is not None else \
                            True
                            # self.all_btn.mouse_clicked(event) if self.all_btn.mouse_clicked(event) else \

    def render_buttons(self) -> None:
        """
        Renders the Start button.
        :return: None
        """
        self.a_star_btn.render()
        self.bfs_btn.render()
        self.dijk_btn.render()
        self.gbfs_btn.render()
        self.human_btn.render()
        # self.all_btn.render()

class BasicMenu(MenuTemplate):
    """
    The Basic class is a default template that can be used for the menu screens. It inherits from MenuTemplate and
    expands on the inherited methods. If different templates are desired, create more classes in this file. This
    Basic class can be used as a template for any future classes.
    """

    def __init__(self, screen: pygame.Surface, font: Font, text_color: str, button_colors: ButtonColors, title: str):
        super().__init__(screen, font, text_color, button_colors)
        self.title: Text = Text(screen, title, 48, color=self.text_color)
        self.title.rect.center = vector_as_tuple(add_vectors(Vector2(*self.screen.get_rect().center),
                                                             Vector2(0, -200)))

    def render_buttons(self) -> None:
        """
        This method calls the inherited method to render the start button. It also renders the title
        :return: None
        """
        super().render_buttons()
        self.title.render()
