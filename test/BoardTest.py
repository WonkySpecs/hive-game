import unittest
from board import Board
from tile import Tile, Creature


class BoardTest(unittest.TestCase):
    def test_is_hive_connected_single_tile_true(self):
        board = Board(Tile(Creature.ANT, 0))
        self.assertTrue(board.is_hive_connected())

    def test_is_hive_connected_two_disconnected_tiles_false(self):
        board = Board(Tile(Creature.ANT, 0))
        board.add_tile(Tile(Creature.ANT, 1), (5, 5))
        self.assertFalse(board.is_hive_connected())

    def test_is_hive_connected_connected_tiles_true(self):
        board = Board(Tile(Creature.ANT, 0))
        board.add_tile(Tile(Creature.ANT, 1), (0, 1))
        self.assertTrue(board.is_hive_connected())

    def test_is_hive_connected_large_connected_true(self):
        board = Board(Tile(Creature.ANT, 0))
        for j in range(1, 50):
            for i in range(20):
                board.add_tile(Tile(Creature.ANT, 1), (i, j))
        self.assertTrue(board.is_hive_connected())

    def test_is_hive_connected_large_unconnected_false(self):
        board = Board(Tile(Creature.ANT, 0))
        board.add_tile(Tile(Creature.ANT, 1), (100, 100))
        for j in range(1, 50):
            for i in range(20):
                board.add_tile(Tile(Creature.ANT, 1), (i, j))
        self.assertFalse(board.is_hive_connected())

    def test_is_hive_connected_ring_connected_true(self):
        board = Board(Tile(Creature.ANT, 0))
        board.add_tile(Tile(Creature.ANT, 1), (1, 0))
        board.add_tile(Tile(Creature.ANT, 1), (1, 1))
        board.add_tile(Tile(Creature.ANT, 1), (1, 2))
        board.add_tile(Tile(Creature.ANT, 1), (0, 2))
        board.add_tile(Tile(Creature.ANT, 1), (-1, 1))
        # Underlying functions shouldn't care about stacked tiles, but worth checking
        board.add_tile(Tile(Creature.BEETLE, 1), (-1, 1))
        self.assertTrue(board.is_hive_connected())

    def test_is_hive_connected_disconnected_components_false(self):
        board = Board(Tile(Creature.ANT, 0))
        board.add_tile(Tile(Creature.ANT, 1), (1, 0))
        board.add_tile(Tile(Creature.ANT, 1), (1, 1))
        board.add_tile(Tile(Creature.BEETLE, 1), (1, 1))

        board.add_tile(Tile(Creature.ANT, 1), (1, -2))
        board.add_tile(Tile(Creature.ANT, 1), (0, -2))

        board.add_tile(Tile(Creature.ANT, 1), (2, -1))
        board.add_tile(Tile(Creature.ANT, 1), (3, 0))
        self.assertFalse(board.is_hive_connected())
