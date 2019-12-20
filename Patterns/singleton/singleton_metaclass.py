
#singleton using a metaclass
class Singleton(type):
	__instances={}

	def __call__(cls, *args, **kwargs):
		if cls not in cls.__instances:
			cls.__instances[cls]=super(Singleton, cls).__call__(*args, **kwargs)
		return cls.__instances[cls]


class Database(metaclass=Singleton):
	def __init__(self):
		print('loading database')


#test
d1=Database()
d2=Database()
print(hex(id(d1)))
print(hex(id(d2)))
print(d1==d2)