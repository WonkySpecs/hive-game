from tile import Tile, Creature

class Board:
	def __init__(self, first_tile):
		self.grid = { (0, 0) : first_tile }

	def add_tile(self, tile, coordinate):
		self.grid[coordinate] = tile

	def remove_tile(self, coordinate):
		self.grid[coordinate] = Creature.BLANK

	def neighbours(self, coordinate):
		(i, j) = coordinate
		neighbouring_coordinates = [(i - 1, j + 1), (i - 1, j), (i - 1, j - 1), (i, j + 1), (i + 1, j),(i, j - 1)]
		return [self.grid.get((x, y), Tile(Creature.BLANK, 1)) for (x, y) in neighbouring_coordinates]

	def __iter__(self):
		return iter(self.grid.items())