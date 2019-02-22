from player import Player
from board import Board


class GameState:
    def __init__(self):
        self.players = [Player(), Player()]
        self.player_turn = 0
        self.board = Board()

    def calculate_winner(self):
        winners = []
        [queen1, queen2] = self.board.get_queen_coordinates()
        if queen1 and self.board.is_surrounded(queen1):
            winners.append(2)

        if queen2 and self.board.is_surrounded(queen2):
            winners.append(1)

        return winners if winners else None

    def is_valid_move(self, move):
        return True

    def next_player_turn(self):
        self.player_turn = (self.player_turn + 1) % len(self.players)
