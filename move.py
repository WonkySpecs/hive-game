from enum import Enum, auto
from tile import Creature, Tile
from board import Board


class MoveType(Enum):
    PLACE = auto()
    MOVE = auto()


class Move:
    def __init__(self, move_type, tile_identifier, target_coordinate):
        self.move_type = move_type
        self.tile_identifier = tile_identifier
        self.target_coordinate = target_coordinate
        self._validate()

    def _validate(self):
        if self.move_type == MoveType.PLACE:
            if type(self.tile_identifier) != Creature:
                raise AttributeError(
                    "For a PLACE Move, first parameter must be a Creature. Was '" + self.tile_identifier + '"')

        elif self.move_type == MoveType.MOVE:
            if type(self.tile_identifier) != tuple:
                raise AttributeError(
                    "For a PLACE Move, first parameter must be a tuple. Was '" + self.tile_identifier + '"')
        else:
            raise AttributeError("Move 'type' must be a MoveType. Was '" + self.move_type + "'")

    def translate_to_board_function(self):
        if self.move_type == MoveType.PLACE:
            return lambda board, player: Board.add_tile(board, Tile(self.tile_identifier, player),
                                                        self.target_coordinate)
        elif self.move_type == MoveType.MOVE:
            return lambda board, player: Board.move_tile(board, self.tile_identifier, self.target_coordinate)

    def __str__(self):
        return f"Move - {self.move_type} {self.tile_identifier}, target_coordinate {self.target_coordinate}"
