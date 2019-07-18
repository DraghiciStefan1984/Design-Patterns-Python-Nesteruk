from abc import ABC


class State(ABC):
	def on(self, switch):
		print('Light is already on.')
		
	def off(self, switch):
		print('Light is already off.')
		
		
class OnState(State):
	def __init__(self):
		print('Light is turned on.')
		
	def off(self, switch):
		print('Turning light off...')
		switch.state=OffState()
		
		
class OffState(State):
	def __init__(self):
		print('Light is turned off.')
		
	def on(self, switch):
		print('Turning light on...')
		switch.state=OnState()


class Switch:
	def __init__(self):
		self.state=OffState()
		
	def on(self):
		self.state.on(self)
		
	def off(self):
		self.state.off(self)
		
		
#test
s=Switch()
s.on()
s.off()
s.off()