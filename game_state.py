from player import Player
from board import Board


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

    def next_player_turn(self):
        self.player_turn = (self.player_turn + 1) % len(self.players)

    def is_placement_legal(self, tile_creature, coordinate):
        if tile_creature not in self.players[self.player_turn].unplaced_creatures:
            return False, f"Tile {tile_creature} not available for player to place"

        if not self.board.queen_coordinates[self.player_turn] \
                and (len(self.move_history) - self.player_turn) / len(self.players) >= 3:
            return False, "Player must place queen in first 4 moves"

        if self.board.get_tile_at(coordinate):
            return False, "Tile must be placed in an empty space"

        if len(self.move_history) < len(self.players):
            return True, "First move is not restricted by placement rules"

        neighbours = self.board.get_neighbouring_tiles(coordinate)
        friendly_piece_adjacent = False

        for neighbouring_tile in neighbours:
            if neighbouring_tile:
                if neighbouring_tile.player != self.player_turn:
                    return False, "Tile cannot be placed touching opponents piece"
                else:
                    friendly_piece_adjacent = True

        return friendly_piece_adjacent, "Tile must be placed touching a friendly piece"

    def is_movement_legal(self, start_coordinate, end_coordinate):
        return True
