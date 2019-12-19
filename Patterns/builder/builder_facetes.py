
class Person:
	def __init__(self):
		self.street_address=None
		self.postcode=None
		self.city=None
		self.company_name=None
		self.position=None
		self.annual_income=None
		
	def __str__(self):
		return f'Address: {self.street_address}, {self.postcode}, {self.city}' + f'\nEmployed at {self.company_name} as a {self.position} earning {self.annual_income} per year.'
		
		
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
		
	def at(self, company_name):
		self.person.company_name=company_name
		return self
		
	def as_a(self, position):
		self.person.position=position
		return self
		
	def earning(self, annual_income):
		self.person.annual_income=annual_income
		return self
		
		
class PersonAddressBuilder(PersonBuilder):
	def __init__(self, person):
		super().__init__(person)
		
	def lives_at(self, street_address):
		self.person.street_address=street_address
		return self
		
	def with_postcode(self, postcode):
		self.person.postcode=postcode
		return self
		
	def city(self, city):
		self.person.city=city
		return self
		
		
#test
pb=PersonBuilder()
person=pb.lives.lives_at('Racovita').with_postcode('484153').city('Bucharest').works.at('My company').as_a('CEO').earning(485135000).build()
print(person)
