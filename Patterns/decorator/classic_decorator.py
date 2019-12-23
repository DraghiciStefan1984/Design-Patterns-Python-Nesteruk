from abc import ABC


class Shape(ABC):
	def __str__(self):
		return ''
		
		
class Circle(Shape):
	def __init__(self, radius):
		self.radius=radius
		
	def resize(self, factor):
		self.radius*=factor
		
	def __str__(self):
		return f'a circle of radius {self.radius}'
		
		
class Square(Shape):
	def __init__(self, side):
		self.side=side
		
	def __str__(self):
		return f'a square with side of {self.side}'
		
		
class ColoredShape(Shape):
	def __init__(self, shape, color):
		self.color=color
		self.shape=shape
		
	def __str__(self):
		return f'a {self.shape} of color {self.color}.'
		
		
class TransparentShape(Shape):
	def __init__(self, shape, transparency):
		self.shape=shape
		self.transparency=transparency
		
	def __str__(self):
		return f'{self.shape} has {self.transparency*100}% transparency.'
		
		
#test
c=Circle(2)
print(c)
red_c=ColoredShape(c, 'red')
print(red_c)
red_half_transp_c=TransparentShape(red_c, .535)
print(red_half_transp_c)