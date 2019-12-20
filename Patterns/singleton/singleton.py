
class Database:
	__instance=None

	def __init__(self):
		print('Loading db from file')

	#redefine the allocator
	def __new__(cls, *args, **kwargs):
		if not cls.__instance:
			cls.__instance=super(Database, cls).__new__(cls, *args, **kwargs)
		return cls.__instance


#test
d1=Database()
d2=Database()
print(hex(id(d1)))
print(hex(id(d2)))
print(d1==d2)