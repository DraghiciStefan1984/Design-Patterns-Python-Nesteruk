import copy

class Address:
	def __init__(self, suite, city, postcode):
		self.suite=suite
		self.city=city
		self.postcode=postcode
		
	def __str__(self):
		return f'{self.suite}, {self.city}, {self.postcode}'
		
		
class Employee:
	def __init__(self, name, address):
		self.name=name
		self.address=address
		
	def __str__(self):
		return f'{self.name} works at {self.address}.'
		
		
class EmployeeFactory:
	main_office_employee=Employee('', Address('Racovita', 'Bucuresti', 13245)) 
	aux_office_employee=Employee('', Address('Unirii', 'Bucuresti', 24511))
	
	@staticmethod
	def __new_employee(proto, name, suite):
		result=copy.deepcopy(proto)
		result.address.suite=suite
		result.name=name
		return result
	
	@staticmethod
	def new_main_office_employee(name, suite):
		return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)
		
	@staticmethod
	def new_aux_office_employee(name, suite):
		return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)
		
#test
john=EmployeeFactory.new_main_office_employee('John', 101)
print(john)