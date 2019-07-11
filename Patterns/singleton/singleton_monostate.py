import random


class Monostate:
	_shared_state={}
	
	def __new__(cls, *args, **kwargs):
		obj=super(Monostate, cls).__new__(cls, *args, **kwargs)
		obj.__dict__=cls._shared_state
		return obj
		
		
class CFO(Monostate):
	def __init__(self):
		self.name=''
		self.money_managed=0
		
	def __str__(self):
		return f'{self.name} manages {self.money_managed}$.'
		

'''
class CEO:
	__shared_state={'name':'Stefan', 'age':35}
	
	def __init__(self):
		self.__dict__=self.__shared_state
		
	def __str__(self):
		return f'{self.name} is {self.age} old.'
'''
	
	
#test
c1=CFO()
c1.name='Stef'
c1.money_managed=1000000
print(c1)

c2=CFO()
c2.name='Ana'
c2.money_managed=150000
print(c1)
print(c2)
print(hex(id(c1)))
print(hex(id(c2)))