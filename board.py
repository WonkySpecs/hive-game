from tile import Creature
from stack import Stack

class Board:
	def __init__(self, first_tile):
		self.grid = dict()
		self.queen_coordinates = [None, None]
		self.add_tile(first_tile, (0, 0))

	def add_tile(self, tile, coordinate):
		if tile.creature == Creature.QUEEN:
			self.queen_coordinates[tile.player] = coordinate
		try:
			self.grid[coordinate].push(tile)
		except KeyError:
			self.grid[coordinate] = Stack(tile)

	def remove_tile(self, coordinate):
		self.grid[coordinate].pop()

	def tile_at(self, coordinate):
		try:
			return self.grid.get(coordinate).top()
		except AttributeError:
			self.grid[coordinate] = Stack()
			return None

	def neighbours(self, coordinate):
		(i, j) = coordinate
		neighbouring_coordinates = [(i - 1, j + 1), (i - 1, j), (i - 1, j - 1), (i, j + 1), (i + 1, j),(i, j - 1)]
		return [self.tile_at((x, y)) for (x, y) in neighbouring_coordinates]

	def is_surrounded(self, coordinate):
		for neighbour in self.neighbours(coordinate):
			if not neighbour:
				return False

		return True

	def get_queen_coordinates(self):
		return self.queen_coordinates

	def __iter__(self):
		return iter(self.grid.items())