from game_state import GameState


class Game:
	def __init__(self, player_input_generators):
		self.game_state = GameState()
		self.player_inputs = player_input_generators

	def play(self):
		print("Playing")

		while not self.game_state.calculate_winner():
			move = next(self.player_inputs[self.game_state.player_turn])
			legal, msg = move.is_legal(self.game_state)
			if legal:
				self.game_state.execute(move)
			else:
				print("Illegal move: " + msg)
			print(self.game_state.board)

		print(f"Player(s) {self.game_state.calculate_winner()} won")

	def get_game_history(self):
		history = ""
		counter = 1
		for move in self.game_state.move_history:
			history += f"Move {counter}: {move}\n"
			counter += 1
		return history
