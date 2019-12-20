
class CEO:
	__shared_state={'name':'Steve', 'age':35}
	
	def __init__(self):
		self.__dict__=self.__shared_state
		
	def __str__(self):
		return f'{self.name} is {self.age} years old.'
		
		
class Monostate:
	__shared_state={}
	
	def __new__(cls, *args, **kwargs):
		obj=super(Monostate, cls).__new__(cls, *args, **kwargs)
		obj.__dict__=cls.__shared_state
		return obj
		
		
class CFO(Monostate):
	def __init__(self):
		self.name=''
		self.money_managed=0
		
	def __str__(self):
		return f'{self.name} manages ${self.money_managed} dollars.'

#test
ceo1=CEO()
ceo2=CEO()
ceo2.age=80
print(hex(id(ceo1)))
print(hex(id(ceo2)))
print(ceo1==ceo2)


cfo1=CFO()
cfo1.name='Mike'
cfo1.money_managed=125000
cfo2=CFO()
cfo2.name='Ana'
cfo2.money_managed=78500
print(hex(id(cfo1)))
print(hex(id(cfo2)))
print(cfo1==cfo2)