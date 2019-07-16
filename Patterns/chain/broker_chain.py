from enum import Enum
from abc import ABC


class Event(list):
	def __call__(self, *args, **kwargs):
		for item in self:
			item(*args, **kwargs)
			
			
class WhatToQuery(Enum):
	ATTACK=1
	DEFENSE=2
	
	
class Query:
	def __init__(self, creature_name, what_to_query, default_value):
		self.creature_name=creature_name
		self.what_to_query=what_to_query
		self.value=default_value
	
			
class Game:
	def __init__(self):
		self.queries=Event()
		
	def perform_query(self, sender, query):
		self.queries(sender, query)
			
			
class Creature:
	def __init__(self, game, name, attack, defense):
		self.game=game
		self.name=name
		self.init_attack=attack
		self.init_defense=defense
		
	@property
	def attack(self):
		q=Query(self.name, WhatToQuery.ATTACK, self.init_attack)
		self.game.perform_query(self, q)
		return q.value
		
	@property
	def defense(self):
		q=Query(self.name, WhatToQuery.DEFENSE, self.init_defense)
		self.game.perform_query(self, q)
		return q.value
		
	def __str__(self):
		return f'{self.name} ({self.attack}/{self.defense})'
		
		
class CreatureModifier(ABC):
	def __init__(self, game, creature):
		self.creature=creature
		self.game=game
		self.game.queries.append(self.handle)
		
	def handle(self, sender, query):
		pass
		
	def __enter__(self):
		return self
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.game.queries.remove(self.handle)
		
		
class DoubleAttackModifier(CreatureModifier):
	def handle(self, sender, query):
		if sender.name==self.creature.name and query.what_to_query==WhatToQuery.ATTACK:
			query.value*=2
			
			
class DoubleDefenseModifier(CreatureModifier):
	def handle(self, sender, query):
		if sender.name==self.creature.name and query.what_to_query==WhatToQuery.DEFENSE:
			query.value*=2
		
		
#test
game=Game()
goblin=Creature(game, 'Goblin', 20, 20)
print(goblin)
dam=DoubleAttackModifier(game, goblin)
print(goblin)
with DoubleDefenseModifier(game, goblin):
	print(goblin)
print(goblin)