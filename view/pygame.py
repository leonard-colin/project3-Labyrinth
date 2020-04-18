import os
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

    def __init__(self, lines, columns):
        """Function to initialize labyrinth in Pygame"""

        pygame.init()
        self.window_size = (columns * 20, lines * 20)  # (x, y)
        self.screen_surface = pygame.display.set_mode(self.window_size)
        self.cambria_font = pygame.font.SysFont('Cambria', 30)
        self.quit_text = self.cambria_font.render("Press any key to quit",
                                                  True, (255, 255, 255))

        self.floor = pygame.image.load(self._resource_path('floor.png')
                                       ).convert_alpha()
        self.wall = pygame.image.load(self._resource_path('wall.png')
                                      ).convert_alpha()
        self.needle = pygame.image.load(self._resource_path('needle.png')
                                        ).convert_alpha()
        self.tube = pygame.image.load(self._resource_path('tube.png')
                                      ).convert_alpha()
        self.ether = pygame.image.load(self._resource_path('ether.png')
                                       ).convert_alpha()
        self.macgyver = pygame.image.load(self._resource_path('MacGyver.png')
                                          ).convert_alpha()
        self.guardian = pygame.image.load(self._resource_path('Gardien.png'))\
            .convert_alpha()

    def _resource_path(self, file):
        """Function to access resources"""

        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resource', file)

    def display_lab(self, lab):
        """Function that displays labyrinth and its characters and tools"""

        self.screen_surface.blit(self.macgyver, (3 * 20, 1 * 20))
        self.screen_surface.blit(self.guardian, (13 * 20, 13 * 20))

        for x, line in enumerate(lab):
            for y, element in enumerate(line):
                if element == '#':  # If element is a wall
                    self.screen_surface.blit(self.wall, (y * 20, x * 20))
                elif element == ' ':  # If element is a free path
                    self.screen_surface.blit(self.floor, (y * 20, x * 20))
                elif element == 'M':  # If element is Mac Gyver
                    self.screen_surface.blit(self.floor, (y * 20, x * 20))
                    self.screen_surface.blit(self.macgyver, (y * 20, x * 20))
                elif element == 'N':  # If element is needle tool
                    self.screen_surface.blit(self.needle, (y * 20, x * 20))
                elif element == 'T':  # If element is tube tool
                    self.screen_surface.blit(self.tube, (y * 20, x * 20))
                elif element == 'E':  # If element is ether tool
                    self.screen_surface.blit(self.ether, (y * 20, x * 20))

        pygame.display.flip()

    def get_direction(self):
        """Function that gets a direction in labyrinth"""

        moves = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key in self.DIRECTIONS:
                        moves.append(self.DIRECTIONS[event.key])
            return moves

    def win(self):
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

    def lose(self):
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
