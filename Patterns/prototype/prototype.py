import copy

class Address:
	def __init__(self, street, city, postcode):
		self.street=street
		self.city=city
		self.postcode=postcode
		
	def __str__(self):
		return f'{self.street}, {self.city}, {self.postcode}'
		
		
class Person:
	def __init__(self, name, address):
		self.name=name
		self.address=address
		
	def __str__(self):
		return f'{self.name} lives at {self.address}.'
		
		
#test
p1=Person('Stefan', Address('Racovita', 'Bucuresti', 13245))
print(p1)

#prototype pattern uses deep copy to reuse an existing instance
p2=copy.deepcopy(p1)
p2.name='Ana'
print(p2)