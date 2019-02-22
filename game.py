from game_state import GameState


class Game:
	def __init__(self, player_input_generators):
		self.game_state = GameState()
		self.player_inputs = player_input_generators

	def play(self):
		print("Playing")

		while not self.game_state.calculate_winner():
			move = next(self.player_inputs[self.game_state.player_turn])
			if self.game_state.is_valid_move(move):
				move.translate_to_board_function()(self.game_state.board, self.game_state.player_turn)
				self.game_state.next_player_turn()
		print(f"Player(s) {self.game_state.calculate_winner()} won")
