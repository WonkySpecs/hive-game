from enum import Enum, auto

class Creature(Enum):
	QUEEN = auto()
	BEETLE = auto()
	GRASSHOPPER = auto()
	SPIDER = auto()
	ANT = auto()

class Tile:
	def __init__(self, creature, player):
		self.creature = creature
		self.player = player