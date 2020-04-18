import random as r
from constants import TOOLS


class Labyrinth:
    """Class that defines a labyrinth, characterized by:
    - its size
    - Mac Gyver, Guardian and tools positions
    - Mac Gyver's movements
    - logic to win or to lose"""

    def __init__(self, path):
        """Function that initializes a labyrinth"""

        self.lablist = []
        with open(path) as file:
            for line in file:
                # The '/' allows to see free paths more clearly in 'map.txt'
                result = line.replace('/', ' ')
                result = result.replace('\n', '')
                result = list(result)
                self.lablist.append(result)

    def get_size(self):
        """Function that returns labyrinth's size
        in a tuple (number of lines, number of columns)"""

        return len(self.lablist[0]), len(self.lablist)

    def get_random_position(self):
        """Function that gets a random empty cell
        from a row in column index in labyrinth"""

        possible_positions = []
        for x, line in enumerate(self.lablist):
            for y, element in enumerate(line):
                if element == ' ':
                    possible_positions.append((x, y))
        return r.choice(possible_positions)

    def set_character_position(self, character):
        """Function that sets a random position in a random empty cell
        for a given line"""

        x, y = character.position
        self.lablist[x][y] = character.name

    def __len__(self):
        """Function that returns the number of lines contained in labyrinth"""

        return len(self.lablist)

    def set_tool_positions(self, tools):
        """Function that sets tools random positions"""

        for tool in tools:
            x, y = self.get_random_position()
            self.lablist[x][y] = tool

    def get_new_position(self, macgyver, direction):
        """Function that gets Mac Gyver's next position"""

        position = macgyver.position
        y, x = position
        if direction == 'UP':
            return y - 1, x
        elif direction == 'DOWN':
            return y + 1, x
        elif direction == 'LEFT':
            return y, x - 1
        elif direction == 'RIGHT':
            return y, x + 1
        else:
            return y, x

    def move_macgyver(self, macgyver, guardian, direction):
        """Function that allows macgyver to move in the labyrinth,
        according to walls, guardian and tools positions"""

        y, x = macgyver.position
        new_y, new_x = self.get_new_position(macgyver, direction)
        element = self.lablist[new_y][new_x]
        if element == ' ':
            self.lablist[new_y][new_x] = macgyver.name
            self.lablist[y][x] = ' '
            macgyver.position = (new_y, new_x)
            return {'event': 'CONTINUE'}
        elif element == '#' or (y, x) == (new_y, new_x):
            print("Mac Gyver cannot go through walls!".upper())
            return {'event': 'NO_MOVE'}
        elif element in TOOLS:
            tool = self.lablist[new_y][new_x]
            macgyver.add_tool(tool)
            macgyver.position = (new_y, new_x)
            self.lablist[new_y][new_x] = macgyver.name
            self.lablist[y][x] = ' '
            return {'event': 'ADD_TOOL'}
        elif element == guardian.name:
            if len(macgyver.tools) == len(TOOLS):
                return {'event': 'WIN'}
            else:
                return {'event': 'LOSE'}
