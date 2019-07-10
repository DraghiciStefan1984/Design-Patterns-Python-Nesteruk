from abc import ABC, abstractmethod
from enum import Enum


#models
class HotDrink(ABC):
	@abstractmethod
	def consume(self):
		pass
	

class Tea(HotDrink):
	def consume(self):
		print('This tea is very good!')
		
		
class Coffee(HotDrink):
	def consume(self):
		print('I need coffeeeeeee!')
		
		
#factories
class HotDrinkFactory(ABC):
	@abstractmethod
	def prepare(self, amount):
		pass
		
		
class TeaFactory(HotDrinkFactory):
	def prepare(self, amount):
		print(f'put tea bag, boil water, pour {amount} mls of milk and enjoy.')
		return Tea()
		
		
class CoffeeFactory(HotDrinkFactory):
	def prepare(self, amount):
		print(f'grind some beans, boil water, pour {amount} mls of milk and enjoy.')
		return Coffee()
		
		
class HotDrinkMachine:
	class AvailableDrink(Enum):
		COFFEE=1
		TEA=2
		
	factories=[]
	initialized=False
		
	def __int__(self):
		if not self.initialized:
			self.initialized=True
			for d in self.AvailableDrink:
				name=d.name[0]+d.name[1:].lower()
				factory_name=name+'Factory'
				factory_instance=eval(factory_name)()
				self.factories.append((name, factory_instance))
				
	def make_drink(self):
		print('Available drinks:')
		for f in self.factories:
			print(f[0])
		s=input(f'Please pick a drink: ')
		index=int(s)
		s=input(f'Specify amount: ')
		amount=int(s)
		return self.factories[index][1].prepare(amount)



#test
machine=HotDrinkMachine()
machine.make_drink()