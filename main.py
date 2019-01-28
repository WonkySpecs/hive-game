from board import Board
from tile import Tile, Creature
from game_rules import *

game_board = Board(Tile(Creature.QUEEN, 1))
winner = calculate_winner(game_board)

while not winner:
	#get input

	#if place
	#place if possible
	#else if move
	#move if possible
	print("Playing")
	game_board.add_tile(Tile(Creature.SPIDER, 2), (-1, 0))
	print(calculate_winner(game_board))
	game_board.add_tile(Tile(Creature.SPIDER, 1), (1, 0))
	print(calculate_winner(game_board))
	game_board.add_tile(Tile(Creature.SPIDER, 2), (-1, 1))
	print(calculate_winner(game_board))
	game_board.add_tile(Tile(Creature.SPIDER, 1), (0, 1))
	print(calculate_winner(game_board))
	game_board.add_tile(Tile(Creature.SPIDER, 2), (-1, -1))
	print(calculate_winner(game_board))
	game_board.add_tile(Tile(Creature.SPIDER, 1), (0, -1))
	winner = calculate_winner(game_board)
print(winner)