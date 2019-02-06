from tile import Creature, Tile
from stack import Stack
from typing import List, Tuple, Dict


class Board:
    def __init__(self, first_tile: Tile):
        self.grid: Dict[Tuple[int, int], Stack] = dict()
        self.queen_coordinates: List[Tuple[int, int]] = [None, None]
        self.add_tile(first_tile, (0, 0))

    def add_tile(self, tile: Tile, coordinate: Tuple[int, int]):
        if tile.creature == Creature.QUEEN:
            self.queen_coordinates[tile.player] = coordinate
        try:
            self.grid[coordinate].push(tile)
        except KeyError:
            self.grid[coordinate] = Stack(tile)

    def remove_tile(self, coordinate: Tuple[int, int]) -> None:
        self.grid[coordinate].pop()

    def tile_at(self, coordinate: Tuple[int, int]):
        try:
            return self.grid.get(coordinate).top()
        except AttributeError:
            self.grid[coordinate] = Stack()
            return None

    def neighbours(self, coordinate: Tuple[int, int]) -> List[Tile]:
        (i, j) = coordinate
        neighbouring_coordinates = [(i - 1, j + 1), (i - 1, j), (i - 1, j - 1), (i, j + 1), (i + 1, j), (i, j - 1)]
        return [self.tile_at((x, y)) for (x, y) in neighbouring_coordinates]

    def is_surrounded(self, coordinate: Tuple[int, int]) -> bool:
        for neighbour in self.neighbours(coordinate):
            if not neighbour:
                return False

        return True

    def get_queen_coordinates(self) -> List:
        return self.queen_coordinates

    def __iter__(self):
        return iter(self.grid.items())
