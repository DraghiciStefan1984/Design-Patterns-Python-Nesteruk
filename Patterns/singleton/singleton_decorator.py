import random

#the decorator
def singleton_decorator(class_):
	instances={}
	
	def get_instance(*args, **kwargs):
		if class_ not in instances:
			instances[class_]=class_(*args, **kwargs)
		return instances[class_]
	
	return get_instance
	

@singleton_decorator
class Database:
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