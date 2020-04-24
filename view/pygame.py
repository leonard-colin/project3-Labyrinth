import os
from typing import List, Union

import pygame


class Pygame:
    """Class that defines Pygame initialization, characterized by:
    - the display of the labyrinth
    - get a direction in the labyrinth
    - win and lose messages to end the game"""

    DIRECTIONS = {pygame.K_UP: 'UP',
                  pygame.K_DOWN: 'DOWN',
                  pygame.K_LEFT: 'LEFT',
                  pygame.K_RIGHT: 'RIGHT'}

    def __init__(self, lines: int, columns: int):
        """Function to initialize labyrinth in Pygame"""

        pygame.init()
        self.window_size = (columns * 20, lines * 20)  # (x, y)
        self.screen_surface = pygame.display.set_mode(self.window_size)
        self.cambria_font = pygame.font.SysFont('Cambria', 30)
        self.quit_text = self.cambria_font.render("Press any key to quit",
                                                  True, (255, 255, 255))

        self.floor = pygame.image.load(self._resource_path('floor.png'))\
            .convert_alpha()
        self.wall = pygame.image.load(self._resource_path('wall.png'))\
            .convert_alpha()
        self.needle = pygame.image.load(self._resource_path('needle.png'))\
            .convert_alpha()
        self.tube = pygame.image.load(self._resource_path('tube.png'))\
            .convert_alpha()
        self.ether = pygame.image.load(self._resource_path('ether.png'))\
            .convert_alpha()
        self.macgyver = pygame.image.load(self._resource_path('MacGyver.png'))\
            .convert_alpha()
        self.guardian = pygame.image.load(self._resource_path('Gardien.png'))\
            .convert_alpha()

    def _resource_path(self, file: str) -> str:
        """Function to access resources"""

        return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '../resource', file)

    def display_lab(self, lab: List[List[str]]):
        """Function that displays labyrinth and its characters and tools"""

        square_size = 20
        for x, line in enumerate(lab):
            for y, element in enumerate(line):
                if element == '#':  # If element is a wall
                    self.screen_surface.blit(self.wall, (y * square_size,
                                                         x * square_size))
                elif element == ' ':  # If element is a free path
                    self.screen_surface.blit(self.floor, (y * square_size,
                                                          x * square_size))
                elif element == 'M':  # If element is Mac Gyver
                    self.screen_surface.blit(self.floor, (y * square_size,
                                                          x * square_size))
                    self.screen_surface.blit(self.macgyver, (y * square_size,
                                                             x * square_size))
                elif element == 'G':  # If element is Guardian
                    self.screen_surface.blit(self.guardian, (y * square_size,
                                                             x * square_size))
                elif element == 'N':  # If element is needle tool
                    self.screen_surface.blit(self.needle, (y * square_size,
                                                           x * square_size))
                elif element == 'T':  # If element is tube tool
                    self.screen_surface.blit(self.tube, (y * square_size,
                                                         x * square_size))
                elif element == 'E':  # If element is ether tool
                    self.screen_surface.blit(self.ether, (y * square_size,
                                                          x * square_size))

        pygame.display.flip()

    def get_direction(self) -> Union[None, List[str]]:
        """Function that gets a direction in labyrinth"""

        moves = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key in self.DIRECTIONS:
                    moves.append(self.DIRECTIONS[event.key])
        return moves

    def win(self) -> None:
        """Function that displays a 'win' message"""

        win_text = self.cambria_font.render("Congratulation, you win!",
                                            True, (0, 255, 0))
        self.screen_surface.blit(win_text, (30, 140))
        self.screen_surface.blit(self.quit_text, (50, 160))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.KEYDOWN):
                    return None

    def lose(self) -> None:
        """Function that displays a 'lose' message """

        lose_text = self.cambria_font.render("Sorry, but you died!",
                                             True, (255, 0, 0))
        self.screen_surface.blit(lose_text, (55, 140))
        self.screen_surface.blit(self.quit_text, (50, 160))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.KEYDOWN):
                    return None
