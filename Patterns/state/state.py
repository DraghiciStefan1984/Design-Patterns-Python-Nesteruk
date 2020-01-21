from abc import ABC

class Switch:
	def __init__(self):
		self.state=OffState()
		
	def on(self):
		self.state.on(self)
		
	def off(self):
		self.state.off(self)
		
		
class State(ABC):
	def on(self, switch):
		print('light is already on.')
		
	def off(self, switch):
		print('light is already off.')
		
		
class OnState(State):
	def __init__(self):
		print('turning light on.')
		
	def off(self, switch):
		print('turning light off.')
		switch.state=OffState()
		
		
class OffState(State):
	def __init__(self):
		print('turning light off.')
		
	def on(self, switch):
		print('turning light on.')
		switch.state=OnState()
		
		
#test
sw=Switch()
sw.on()
sw.off()
sw.off()
