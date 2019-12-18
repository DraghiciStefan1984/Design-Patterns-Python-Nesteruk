from enum import Enum


class Color(Enum):
	RED=1
	GREEN=2
	BLUE=3
	
	
class Size(Enum):
	SMALL=1
	MEDIUM=2
	LARGE=3
	
	
class Product:
	def __init__(self, name, color, size):
		self.name=name
		self.color=color
		self.size=size
		
		
class ProductFilter:
	def filter_by_color(self, products, color):
		for p in products:
			if p.color==color:
				yield p
				
	def filter_by_size(self, products, size):
		for p in products:
			if p.size==size:
				yield p
				
	def filter_by_size_and_color(self, products, size, color):
		for p in products:
			if p.size==size and p.color==color:
				yield p
				
				
class Specification:
	def is_satisfied(self, item):
		pass
		
		
class Filter:
	def filter(self, items, spec):
		pass
		
		
class ColorSpecification(Specification):
	def __init__(self, color):
		self.color=color
		
	def is_satisfied(self, item):
		return self.color==item.color
		
		
class SizeSpecification(Specification):
	def __init__(self, size):
		self.size=size
		
	def is_satisfied(self, item):
		return self.size==item.size
		
		
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
			

#test
apple=Product('apple', Color.RED, Size.SMALL)
lemon=Product('lemon', Color.GREEN, Size.SMALL)
house=Product('house', Color.BLUE, Size.LARGE)
plane=Product('plane', Color.BLUE, Size.LARGE)
car=Product('car', Color.RED, Size.MEDIUM)
tree=Product('tree', Color.GREEN, Size.MEDIUM)

products=[apple, lemon, house, plane, car, tree]

#old filter
pf=ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
	print(f'{p.name} is green')

#better filter
bf=BetterFilter()
green=ColorSpecification(Color.GREEN)
print('Green products (new):')
for p in bf.filter(products, green):
	print(f'{p.name} is green')

large=SizeSpecification(Size.LARGE)
print('large products (new):')
for p in bf.filter(products, large):
	print(f'{p.name} is large')

#and specification
print('blue large items')
large_blue=AndSpecification(SizeSpecification(Size.LARGE), ColorSpecification(Color.BLUE))
f=BetterFilter()
for p in f.filter(products, large_blue):
	print(f'{p.name} is large and blue')