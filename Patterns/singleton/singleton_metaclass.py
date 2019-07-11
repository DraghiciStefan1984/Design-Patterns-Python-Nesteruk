import random

class Singleton(type):
	_instances={}
	
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls]=super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]
		
		
class Database(metaclass=Singleton):
	def __init__(self):
		print('create a new instance')
		id=random.randint(1, 101)
		print(id)

		
#test
d1=Database()
d2=Database()
print(d1==d2)
print(hex(id(d1)))
print(hex(id(d2)))