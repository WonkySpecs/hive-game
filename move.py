from enum import Enum, auto
from tile import Creature, Tile
from board import Board


class MoveType(Enum):
    PLACE = auto()
    MOVE = auto()


class Move:
    def __init__(self, move_type, param1, param2):
        self.move_type = move_type
        self.param1 = param1
        self.param2 = param2
        self._validate()

    def _validate(self):
        if self.move_type == MoveType.PLACE:
            if type(self.param1) != Creature:
                raise AttributeError("For a PLACE Move, first parameter must be a Creature. Was '" + self.param1 + '"')

        elif self.move_type == MoveType.MOVE:
            if type(self.param1) != tuple:
                raise AttributeError("For a PLACE Move, first parameter must be a tuple. Was '" + self.param1 + '"')
        else:
            raise AttributeError("Move 'type' must be a MoveType. Was '" + self.move_type + "'")

    def translate_to_board_function(self):
        if self.move_type == MoveType.PLACE:
            return lambda board, player: Board.add_tile(board, Tile(self.param1, player), self.param2)
        elif self.move_type == MoveType.MOVE:
            return lambda board, player: Board.move_tile(board, self.param1, self.param2)
