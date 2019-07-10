
class Person:
	def __init__(self):
		self.name=None
		self.date_of_birth=None
		self.position=None
		
	def __str__(self):
		return f"{self.name}, {self.date_of_birth}, {self.position}"
		
	@staticmethod
	def new():
		return PersonBuilder()
		
		
class PersonBuilder:
	def __init__(self):
		self.person=Person()
		
	def build(self):
		return self.person
		
		
class PersonInfoBuilder(PersonBuilder):
	def called(self, name):
		self.person.name=name
		return self
		
		
class PersonJobBuilder(PersonInfoBuilder):
	def works(self, position):
		self.person.position=position
		return self
		
		
class PersonBirthBuilder(PersonJobBuilder):
	def birth(self, birth):
		self.person.date_of_birth=birth
		return self
		
		
#test
pb=PersonBirthBuilder()
person=pb.called('Stefan').works('CEO').birth(10).build()
print(person)
