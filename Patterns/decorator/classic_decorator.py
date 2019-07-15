from abc import ABC


class Shape(ABC):
	def __str__(self):
		return 'Shape'
		
		
class Circle(Shape):
	def __init__(self, radius):
		self.radius=radius
		
	def resize(self, factor):
		self.radius*=factor
		
	def __str__(self):
		return f'Circle of size {self.radius}.'
		
		
class Square(Shape):
	def __init__(self, side):
		self.side=side
		
	def __str__(self):
		return f'Circle of side {self.side}.'
		
		
class ColoredShape(Shape):
	def __init__(self, shape, color):
		self.shape=shape
		self.color=color
		
	def __str__(self):
		return f'{self.shape} has the color of {self.color}.'
		
		
class TransparentShape(Shape):
	def __init__(self, shape, transparency):
		self.shape=shape
		self.transparency=transparency
		
	def __str__(self):
		return f'{self.shape} has {self.transparency}% transparency.'
		
		
#test
circle=ColoredShape(TransparentShape(Circle(5), 25), 'red')
#print(circle)
#circle=ColoredShape(circle, 'red')
#circle=TransparentShape(circle, 25)
print(circle)