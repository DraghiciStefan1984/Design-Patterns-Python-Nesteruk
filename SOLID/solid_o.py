from enum import Enum
from abc import ABC, abstractmethod

class Color(Enum):
	RED=1
	GREEN=2
	BLUE=3


class Size(Enum):
	SMALL=1
	MEDIUM=2
	BIG=3
	
	
class Product:
	def __init__(self, name, color, size):
		self.name=name
		self.size=size
		self.color=color
		
	def __str__(self):
		return f'{self.name}, {self.color}, {self.size}'
		
		
class Specification(ABC):
	@abstractmethod
	def is_satisfied(self, item):
		pass
		
	def __and__(self, other):
		return AndSpecification(self, other)
	

class Filter(ABC):
	@abstractmethod
	def filter(self, items, spec):
		pass
		
		
class ColorSpecification(Specification):
	def __init__(self, color):
		self.color=color
		
	def is_satisfied(self, item):
		return item.color==self.color
		
		
class SizeSpecification(Specification):
	def __init__(self, size):
		self.size=size
		
	def is_satisfied(self, item):
		return item.size==self.size
		
		
class AndSpecification(Specification):
	def __init__(self, spec1, spec2):
		self.spec1=spec1
		self.spec2=spec2
		
	def is_satisfied(self, item):
		return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)
		
		
class BetterFilter(Filter):
	def filter(self, items, spec):
		for item in items:
			if spec.is_satisfied(item):
				yield item
		

'''
#this class violates the Open-Closed principle, not to be used
class ProductFilter:
	def filter_by_color(self, products, color):
		for p in products:
			if p.color==color:
				yield p
				
	def filter_by_size(self, products, size):
		for p in products:
			if p.size==size:
				yield p
'''

	
#test
apple=Product('apple', Color.GREEN, Size.MEDIUM)
melon=Product('melon', Color.GREEN, Size.BIG)
berry=Product('berry', Color.BLUE, Size.SMALL)
tomato=Product('tomato', Color.RED, Size.MEDIUM)

products=[apple, melon, berry, tomato]

bf=BetterFilter()
filtered_items=bf.filter(products, ColorSpecification(Color.GREEN))
for item in filtered_items:
	print(item)

filtered_items=bf.filter(products, SizeSpecification(Size.MEDIUM))
for item in filtered_items:
	print(item)

'''
filtered_items=bf.filter(products, AndSpecification(Size.MEDIUM, Size.BIG))
for item in filtered_items:
	print(item)
'''
