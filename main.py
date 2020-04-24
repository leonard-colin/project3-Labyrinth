from typing import Union

from model.labyrinth import Labyrinth
from model.character import Character
import constants
import argparse
from view.pygame import Pygame
from view.cli import CLI


class Main:
    """Class that initializes labyrinth and defines game logic
    with its game loop"""

    def __init__(self):
        """Class constructor"""

        self.lab = Labyrinth('resource/map.txt')
        macgyver = Character('M', 1, 3)
        guardian = Character('G', 13, 13)
        self.lab.set_character_position(macgyver)
        self.lab.set_character_position(guardian)
        self.lab.set_tool_positions(constants.TOOLS)

        view = self.initialize_view()

        view.display_lab(self.lab.lablist)

        game_loop = True
        while game_loop:
            direction = view.get_direction()

            if direction is None:  # exit key pressed
                exit()

            for d in direction:
                move = self.lab.move_macgyver(macgyver,
                                              guardian,
                                              d)
                if move in ['CONTINUE', 'ADD_TOOL']:
                    view.display_lab(self.lab.lablist)
                elif move == 'NO_MOVE':
                    continue
                elif move == 'WIN':
                    view.win()
                    game_loop = False
                    exit()
                elif move == 'LOSE':
                    view.lose()
                    game_loop = False
                    exit()

    def initialize_view(self) -> Union[CLI, Pygame]:
        parser = argparse.ArgumentParser()
        parser.add_argument('--cli', help="run game in terminal",
                            action="store_true")
        args = parser.parse_args()
        if args.cli:
            view = CLI(*self.lab.get_size())
        else:
            view = Pygame(*self.lab.get_size())
        return view


if __name__ == '__main__':
    Main()
