import copy


class Address:
	def __init__(self, street, city, country):
		self.street=street
		self.city=city
		self.country=country
		
	def __str__(self):
		return f'{self.street}, {self.city}, {self.country}'
		
		
class Person:
	def __init__(self, name, address):
		self.name=name
		self.address=address
		
	def __str__(self):
		return f'{self.name} lives at {self.address}.'
		
		
#test
stef=Person('Stefan', Address('Racovita', '13245', 'Bucharest'))
print(stef)
gabi=copy.deepcopy(stef)
gabi.name='Gabi'
gabi.address.street='Baia de Arama'
print(gabi)
print(stef)