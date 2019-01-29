def calculate_winner(board):
	#find queen, check empty neighbours
	#if none, return other player
	winners = []
	[queen1, queen2] = board.get_queen_coordinates()
	if queen1 and board.is_surrounded(queen1):
		winners.append(2)

	if queen2 and board.is_surrounded(queen2):
		winners.append(1)

	return winners if winners else None