import os

from config import FONT

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import Vector2
from typing import Optional, TypeAlias
from utils import vector_as_tuple

# Typing alias for color
Color: TypeAlias = str | int | tuple[int, int, int, Optional[int]] | list[
    int, int, int, Optional[int]] | pygame.Color


class Text:
    """
    Class that creates text to be displayed in the visualizer.

    Defaults used unless otherwise stated:
    ::
        font       : Bauhaus93
        color      : #daa520          (yellowish)
        position   : Vector(0, 0)     (representing pixels on screen, top left pixel)

    In future projects, defaults for text style should be changed according to style of game for ease of code.
    """

    def __init__(self, screen: pygame.Surface, text: str, font_size: int,
                 color: Color = pygame.Color('#daa520'), position: Vector2 = Vector2(0, 0)):
        """
        :param screen: Screen being used for display. Refer to `here <https://www.pygame.org/docs/ref/surface.html>`_.
        :param text: Font size used for text.
        :param font_size: Font size used for text.
        :param color: Color used for text. Refer to `here <https://www.pygame.org/docs/ref/color.html>`_.
        :param position: Position of text to be displayed Refer to :docs:`vector`.
        """
        self.__is_init = True
        self.screen: pygame.Surface = screen
        self.font_size: int = font_size

        # Get selected font from list of fonts
        self.__font: pygame.font.Font = FONT
        self.color: Color = color
        self.position: Vector2 = position
        self.text: str = text

        # SysFont, adjust size
        # Render text with color
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
        # get rectangle used
        self.__rect: pygame.Rect = self.__text_surface.get_rect()

        # Set top left position of rect to position
        self.__rect.topleft = vector_as_tuple(self.position)
        self.__is_init = False

    # Render text and rectangle to screen
    def render(self) -> None:
        """

        :return: None
        """
        self.position = Vector2(*self.__rect.topleft)
        self.screen.blit(self.__text_surface, self.__rect)

    # Getter methods
    @property
    def screen(self) -> pygame.Surface:
        return self.__screen

    @property
    def text(self) -> str:
        return self.__text

    @property
    def font_size(self) -> int:
        return self.__font_size

    @property
    def color(self) -> pygame.Color:
        return self.__color

    @property
    def position(self) -> Vector2:
        return self.__position

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    # Setter methods
    @screen.setter
    def screen(self, screen: pygame.Surface) -> None:
        if screen is None or not isinstance(screen, pygame.Surface):
            raise ValueError(f'{self.__class__.__name__}.screen must be of type pygame.Surface.')
        self.__screen: pygame.Surface = screen

    @text.setter
    def text(self, text: str) -> None:
        if text is None or not isinstance(text, str):
            raise ValueError(f'{self.__class__.__name__}.text must be a str.')
        self.__text: str = text
        # Reevaluate text
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
        self.__rect: pygame.Rect = self.__text_surface.get_rect()
        self.__rect.topleft = vector_as_tuple(self.position)

    @font_size.setter
    def font_size(self, font_size: int) -> None:
        if font_size is None or not isinstance(font_size, int):
            raise ValueError(f'{self.__class__.__name__}.font_size must be an int.')
        self.__font_size: int = font_size
        if self.__is_init: return

        # Reevaluate text with new font size
        self.__font: pygame.font.Font = FONT
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
        self.__rect: pygame.Rect = self.__text_surface.get_rect()
        self.__rect.topleft = vector_as_tuple(self.position)

    @color.setter
    def color(self, color: Color) -> None:
        try:
            self.__color: pygame.Color = pygame.Color(color)
            if self.__is_init:
                return
            # Reevaluate text with new font color
            self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
            self.__rect: pygame.Rect = self.__text_surface.get_rect()
            self.__rect.topleft = vector_as_tuple(self.position)
        except (ValueError, TypeError):
            raise ValueError(
                f'{self.__class__.__name__}.color must be a one of the following types: str or int or tuple(int, int, '
                f'int, [int]) or list(int, int, int, [int]) or pygame.Color.')

    @position.setter
    def position(self, position: Vector2) -> None:
        if position is None or not isinstance(position, Vector2):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector2.')
        self.__position: Vector2 = position
        if self.__is_init:
            return
        # Reevaluate text position with new position
        self.__rect.topleft = vector_as_tuple(self.position)
