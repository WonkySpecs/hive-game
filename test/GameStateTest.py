import unittest
from game_state import GameState
from move import Move, MoveType
from tile import Tile, Creature
from board import Board
from message_strings import IllegalPlacement


class BoardTest(unittest.TestCase):
    def test_is_placement_legal_first_turn_anything_is_legal(self):
        game_state = GameState()
        for creature in Creature:
            for coord in [(0, 0), (1, 1), (-1, -1), (100, 100), (-50, 50)]:
                self.assertTrue(f"Placing {creature} at {coord} was not legal",
                                game_state.is_placement_legal(creature, coord))

    def test_is_placement_legal_second_turn_adjacent_is_legal(self):
        move = Move(MoveType.PLACE, Creature.QUEEN, (0, 0))
        game_state = GameState()
        game_state.execute(move)

        for coord in Board.get_neighbouring_coordinates((0, 0)):
            result, msg = game_state.is_placement_legal(Creature.ANT, coord)
            self.assertTrue(result)
            self.assertTrue(msg is None)

    def test_is_placement_legal_second_turn_non_adjacent_not_legal(self):
        move = Move(MoveType.PLACE, Creature.QUEEN, (0, 0))
        game_state = GameState()
        game_state.execute(move)

        for coord in [(20, 20), (-2, -2)]:
            result, msg = game_state.is_placement_legal(Creature.ANT, coord)
            self.assertFalse(result)
            self.assertEqual(msg, IllegalPlacement.no_friendly_tile_adjacent)

    def test_is_placement_legal_third_turn_non_adjacent_not_legal(self):
        move1 = Move(MoveType.PLACE, Creature.QUEEN, (0, 0))
        move2 = Move(MoveType.PLACE, Creature.QUEEN, (1, 0))
        game_state = GameState()
        game_state.execute(move1)
        game_state.execute(move2)

        for coord in [(20, 20), (-2, -2)]:
            result, msg = game_state.is_placement_legal(Creature.ANT, coord)
            self.assertFalse(result)
            self.assertEqual(msg, IllegalPlacement.no_friendly_tile_adjacent)

    def test_is_placement_legal_third_turn_adjacent_to_opponent_not_legal(self):
        move1 = Move(MoveType.PLACE, Creature.QUEEN, (0, 0))
        move2 = Move(MoveType.PLACE, Creature.QUEEN, (1, 0))
        game_state = GameState()
        game_state.execute(move1)
        game_state.execute(move2)

        for coord in [(2, 0), (0, 1), (1, 1), (1, -1), (0, -1)]:
            result, msg = game_state.is_placement_legal(Creature.ANT, coord)
            self.assertFalse(result)
            self.assertEqual(msg, IllegalPlacement.opponent_tile_adjacent)

    def test_is_placement_legal_third_turn_on_existing_tile_not_legal(self):
        move1 = Move(MoveType.PLACE, Creature.QUEEN, (0, 0))
        move2 = Move(MoveType.PLACE, Creature.QUEEN, (1, 0))
        game_state = GameState()
        game_state.execute(move1)
        game_state.execute(move2)

        for coord in [(0, 0), (1, 0)]:
            result, msg = game_state.is_placement_legal(Creature.ANT, coord)
            self.assertFalse(result)
            self.assertEqual(msg, IllegalPlacement.space_not_empty)

    def test_is_placement_legal_third_turn_second_queen_not_legal(self):
        move1 = Move(MoveType.PLACE, Creature.QUEEN, (0, 0))
        move2 = Move(MoveType.PLACE, Creature.QUEEN, (1, 0))
        game_state = GameState()
        game_state.execute(move1)
        game_state.execute(move2)
        result, msg = game_state.is_placement_legal(Creature.QUEEN, (-1, 0))
        self.assertFalse(result)
        self.assertEqual(msg, IllegalPlacement.creature_unavailable)
