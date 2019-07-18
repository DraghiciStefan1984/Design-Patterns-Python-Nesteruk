
class Event(list):
	def __call__(self, *args, **kwargs):
		for item in self:
			item(*args, **kwargs)


class Person:
	def __init__(self, name, address):
		self.name=name
		self.address=address
		self.falls_ill=Event()
		
	def catch_a_cold(self):
		self.falls_ill(self.name, self.address)
		
		
def call_doctor(name, address):
	print(f'{name} needs a doctor at {address}')
		
			
#test
p1=Person('Ion', 'Unirii')
p2=Person('Maria', 'Romana')
p1.falls_ill.append(call_doctor)
p2.falls_ill.append(call_doctor)
p1.catch_a_cold()
p2.catch_a_cold()