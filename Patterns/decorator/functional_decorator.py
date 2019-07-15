import time

def timer_decor(func):
	def wrapper():
		start=time.time()
		result=func()
		end=time.time()
		print(f'{func.__name__} took {int((end-start)*1000)} miliseconds to run.')
		return result
	return wrapper
	

@timer_decor
def some_op():
	print('Start operation')
	time.sleep(1)
	print('We are done')
	return 123
	

#test
some_op()