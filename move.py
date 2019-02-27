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
                    f"For a PLACE Move, first parameter must be a Creature. Was '{self.tile_identifier}'")

        elif self.move_type == MoveType.MOVE:
            if type(self.tile_identifier) != tuple:
                raise AttributeError(
                    f"For a PLACE Move, first parameter must be a tuple. Was '{self.tile_identifier}'")
        else:
            raise AttributeError("Move 'type' must be a MoveType. Was '" + self.move_type + "'")

    def execute(self, game_state):
        if self.move_type == MoveType.PLACE:
            game_state.board.add_tile(Tile(self.tile_identifier, game_state.player_turn), self.target_coordinate)
            game_state.players[game_state.player_turn].unplaced_creatures.remove(self.tile_identifier)  # Wary of the amount of nesting here
        elif self.move_type == MoveType.MOVE:
            game_state.board.move_tile(self.tile_identifier, self.target_coordinate)

    def is_legal(self, game_state):
        if self.move_type == MoveType.PLACE:
            return game_state.is_placement_legal(self.tile_identifier, self.target_coordinate)
        elif self.move_type == MoveType.MOVE:
            return game_state.is_movement_legal(self.tile_identifier, self.target_coordinate)

    def __str__(self):
        return f"Move - {self.move_type} {self.tile_identifier}, target_coordinate {self.target_coordinate}"
