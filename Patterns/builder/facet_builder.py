
class Person:
	def __init__(self):
		self.street=None
		self.city=None
		self.postcode=None
		self.company=None
		self.position=None
		self.income=None
		
	def __str__(self):
		return f"{self.street}, {self.city}, {self.postcode}, {self.company}, {self.position}, {self.income}"
		
		
class PersonBuilder:
	def __init__(self, person=Person()):
		self.person=person
		
	@property
	def works(self):
		return PersonJobBuilder(self.person)
		
	@property
	def lives(self):
		return PersonAddressBuilder(self.person)
		
	def build(self):
		return self.person
		
		
class PersonJobBuilder(PersonBuilder):
	def __init__(self, person):
		super().__init__(person)
		
	def at(self, company):
		self.person.company=company
		return self
	
	def asa(self, position):
		self.person.position=position
		return self
		
	def earning(self, income):
		self.person.income=income
		return self
		
		
class PersonAddressBuilder(PersonBuilder):
	def __init__(self, person):
		super().__init__(person)
		
	def street(self, street):
		self.person.street=street
		return self
	
	def city(self, city):
		self.person.city=city
		return self
		
	def postcode(self, postcode):
		self.person.postcode=postcode
		return self
		
		
#test
pb=PersonBuilder()
person=pb.lives.city('Bucharest').street('Racovita').postcode('123456').works.at('Apple').asa('CEO').earning(1500000).build()
print(person)
