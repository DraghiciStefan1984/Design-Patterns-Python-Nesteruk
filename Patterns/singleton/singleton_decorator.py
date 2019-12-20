
#singleton using a decorator
def singleton(_class_):
	instances={}
	
	def get_instance(*args, **kwargs):
		if _class_ not in instances:
			instances[_class_]=_class_(*args, **kwargs)
		return instances[_class_]
	return get_instance
	

@singleton
class Database:
	def __init__(self):
		print('loading database')


#test
d1=Database()
d2=Database()
print(hex(id(d1)))
print(hex(id(d2)))
print(d1==d2)