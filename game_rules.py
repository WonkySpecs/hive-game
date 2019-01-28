from tile import Creature

def calculate_winner(board):
	#find queen, check empty neighbours
	#if none, return other player
	for coordinate, tile in board:
		if tile.creature == Creature.QUEEN:
			if surrounded(board, coordinate):
				if tile.player == 1:
					return 2
				else:
					return 1

	return None

def surrounded(board, coordinate):
	for neighbour in board.neighbours(coordinate):
		if neighbour.creature == Creature.BLANK:
			return False

	return True