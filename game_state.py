from player import Player
from board import Board
from tile import Creature
from message_strings import IllegalPlacement, IllegalMovement


class GameState:
    def __init__(self):
        self.players = [Player(), Player()]
        self.player_turn = 0
        self.board = Board()
        self.move_history = []

    def calculate_winner(self):
        winners = []
        [queen1, queen2] = self.board.get_queen_coordinates()
        if queen1 and self.board.is_surrounded(queen1):
            winners.append(2)

        if queen2 and self.board.is_surrounded(queen2):
            winners.append(1)

        return winners if winners else None

    def execute(self, move):
        move.execute(self)
        self.move_history.append(move)
        self.next_player_turn()

    def next_player_turn(self):
        self.player_turn = (self.player_turn + 1) % len(self.players)

    def is_placement_legal(self, tile_creature, coordinate):
        if tile_creature not in self.players[self.player_turn].unplaced_creatures:
            return False, IllegalPlacement.creature_unavailable

        if not self.board.queen_coordinates[self.player_turn] \
                and (len(self.move_history) - self.player_turn) / len(self.players) >= 3\
                and tile_creature is not Creature.QUEEN:
            return False, IllegalPlacement.queen_placement_required

        if self.board.get_tile_at(coordinate):
            return False, IllegalPlacement.space_not_empty

        if len(self.move_history) < len(self.players):
            return True, None

        neighbours = self.board.get_neighbouring_tiles(coordinate)
        friendly_piece_adjacent = False

        for neighbouring_tile in neighbours:
            if neighbouring_tile:
                if neighbouring_tile.player != self.player_turn:
                    return False, IllegalPlacement.opponent_tile_adjacent
                else:
                    friendly_piece_adjacent = True

        return friendly_piece_adjacent, IllegalPlacement.no_friendly_tile_adjacent

    def is_movement_legal(self, start_coordinate, end_coordinate):
        return True
