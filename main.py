from game import Game
from move import Move, MoveType
from tile import Creature


def player_1_moves():
    moves = [Move(MoveType.PLACE, Creature.QUEEN, (0, 0)),
             Move(MoveType.PLACE, Creature.SPIDER, (1, 0)),
             Move(MoveType.PLACE, Creature.SPIDER, (0, 1)),
             Move(MoveType.PLACE, Creature.SPIDER, (0, -1))]
    for move in moves:
        yield move


def player_2_moves():
    yield Move(MoveType.PLACE, Creature.SPIDER, (-1, 0))
    yield Move(MoveType.PLACE, Creature.QUEEN, (-1, 1))
    yield Move(MoveType.PLACE, Creature.ANT, (-1, -1))
    yield Move(MoveType.PLACE, Creature.QUEEN, (0, 0))


def moves_from_console():
    pass


if __name__ == "__main__":
    game = Game([player_1_moves(), player_2_moves()])
    game.play()
