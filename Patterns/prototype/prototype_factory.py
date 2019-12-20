import copy


class Address:
	def __init__(self, street, suite, city):
		self.street=street
		self.suite=suite
		self.city=city
		
	def __str__(self):
		return f'{self.street}, {self.suite}, {self.city}'
		
		
class Employee:
	def __init__(self, name, address):
		self.name=name
		self.address=address
		
	def __str__(self):
		return f'{self.name} works at {self.address}.'
		
		
class EmployeeFactory:
	main_employee=Employee('', Address('Racovita', 0, 'Bucharest'))
	aux_employee=Employee('', Address('Racovita', 0, 'Bucharest'))
	
	@staticmethod
	def __new_employee(proto, name, suite):
		result=copy.deepcopy(proto)
		result.name=name
		result.address.suite=suite
		return result
		
	@staticmethod
	def new_main_employee(name, suite):
		return EmployeeFactory.__new_employee(EmployeeFactory.main_employee, name, suite)
	
	@staticmethod
	def new_aux_employee(name, suite):
		return EmployeeFactory.__new_employee(EmployeeFactory.aux_employee, name, suite)
	
	
#test
john=EmployeeFactory.new_main_employee('John', 100)
jane=EmployeeFactory.new_aux_employee('Jane', 102)
mike=EmployeeFactory.new_aux_employee('Mike', 112)
print(john)
print(jane)
print(mike)