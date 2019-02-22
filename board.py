from tile import Creature, Tile
from stack import Stack
from typing import List, Tuple, Dict


class Board:
    def __init__(self, first_tile: Tile = None):
        self.grid: Dict[Tuple[int, int], Stack] = dict()
        self.queen_coordinates: List[Tuple[int, int]] = [None, None]
        if first_tile:
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

    def move_tile(self, start_coordinate, end_coordinate):
        tile = self.grid[start_coordinate].pop()
        self.add_tile(tile, end_coordinate)

    def get_tile_at(self, coordinate: Tuple[int, int]):
        try:
            return self.grid.get(coordinate).top()
        except AttributeError:
            self.grid[coordinate] = Stack()
            return None

    def is_surrounded(self, coordinate: Tuple[int, int]) -> bool:
        for neighbour in self.get_neighbouring_tiles(coordinate):
            if not neighbour:
                return False

        return True

    def get_neighbouring_tiles(self, coordinate: Tuple[int, int]) -> List[Tile]:
        return [self.get_tile_at((x, y)) for (x, y) in Board._neighbouring_coordinates(coordinate)]

    @staticmethod
    def _neighbouring_coordinates(coordinate: Tuple[int, int]) -> List[Tuple[int, int]]:
        (i, j) = coordinate
        neighbours = [(i - 1, j), (i + 1, j)]
        if j % 2 == 0:
            neighbours.extend([(i - 1, j + 1), (i, j + 1), (i - 1, j - 1), (i, j - 1)])
        else:
            neighbours.extend([(i, j + 1), (i + 1, j + 1), (i, j - 1), (i, j + 1)])

        return neighbours

    def get_queen_coordinates(self) -> List:
        return self.queen_coordinates

    def is_hive_connected(self) -> bool:
        """returns True if all tiles on the board are connected, otherwise False"""
        num_tiles = 0
        a_coord = None
        for coord, stack in self.grid.items():
            if stack.top():
                num_tiles += 1
                a_coord = coord

        unexplored_coords = {a_coord}
        coords_with_connected_tiles = set()
        while unexplored_coords:
            exploring = unexplored_coords.pop()
            coords_with_connected_tiles.add(exploring)
            for neighbour_coord in self._neighbouring_coordinates(exploring):
                neighbour = self.get_tile_at(neighbour_coord)
                if neighbour and neighbour_coord not in coords_with_connected_tiles:
                    unexplored_coords.add(neighbour_coord)

        return len(coords_with_connected_tiles) == num_tiles
