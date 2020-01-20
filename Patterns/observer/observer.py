class Event(list):
	def __cal__(self, *args, **kwargs):
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
p=Person('Ana', 'Berceni')
p.falls_ill.append(call_doctor)
p.catch_a_cold()
p.falls_ill.append(lambda name: print('{name} needs a doc.'))
p.falls_ill.remove(call_doctor)