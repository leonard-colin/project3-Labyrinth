class Character:
    """Class that defines a character, characterized by:
      - its name
      - its tools"""

    def __init__(self, name: str, x: int, y: int):
        """Class constructor with character's name and tools inventory"""

        self.name = name
        self.tools = []
        self.position = (x, y)

    def add_tool(self, tool: str):
        """Function that adds a tool in character's inventory"""

        if tool in ['N', 'T', 'E']:
            self.tools.append(tool)
