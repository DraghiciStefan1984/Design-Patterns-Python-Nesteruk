from abc import ABC

class Game(ABC):
	def __init__(self, num_of_players):
		self.num_of_players=num_of_players
		self.current_player=0
		
	def run(self):
		self.start()
		while not self.have_winner:
			self.take_turn()
		print(f'player {self.winner} wins!')
		
	def start(self): pass
	
	def take_turn(self): pass
	
	@property
	def have_winner(self): pass
	
	@property
	def winner(self): pass
	
	
class Chess(Game):
	def __init__(self):
		super().__init__(2)
		self.max_turns=10
		self.turn=1
		
	def run(self):
		super().run()
		
	def start(self):
		print('starting a chess game.')
		
	def take_turn(self):
		print(f'turn {self.turn} taken by player {self.current_player}')
		self.turn+=1
		self.current_player=1-self.current_player
		
	
	@property
	def have_winner(self):
		return self.turn==self.max_turns
	
	@property
	def winner(self):
		return self.current_player
		
		
#test
chess=Chess()
chess.run()


