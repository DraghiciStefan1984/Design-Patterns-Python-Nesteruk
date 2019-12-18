
class Rectangle:
	def __init__(self, width, height):
		self.__width=width
		self.__height=height
		
	@property
	def width(self):
		return self.__width
		
	@width.setter
	def width(self, value):
		self.__width=value
		
	@property
	def height(self):
		return self.__height
		
	@height.setter
	def height(self, value):
		self.__height=value
		
	@property
	def area(self):
		return self.width*self.height
		
	def __str__(self):
		return f'width:{self.width} - height{self.height}'
		
		
class Square(Rectangle):
	def __init__(self, size):
		Rectangle().__init__(self, size, size)
		
	@Rectangle.width.setter
	def width(self, value):
		self.__width=self.__height=value
		
	@Rectangle.height.setter
	def height(self, value):
		self.__width=self.__height=value
		
		
def use_rectangle(rc):
	w=rc.width
	rc.height=10
	expected=int(w*10)
	print(f'Expected an area of {expected}, but got {rc.area}')
	
	
#test
rc=Rectangle(2,3)
use_rectangle(rc)

s=Square(4)
use_rectangle(s)