from enum import Enum
from abc import ABC, abstractmethod


class Rectangle:
	def __init__(self, width, height):
		self._width=width
		self._height=height
		
	@property
	def width(self):
		return self._width
		
	@width.setter
	def width(self, value):
		self._width=value
		
	@property
	def height(self):
		return self._height
		
	@height.setter
	def height(self, value):
		self._height=value
		
	@property
	def area(self):
		return self._width*self._height
		
	def __str__(self):
		return f'width:{self.width}, height:{self.height}'
		
		
class Square(Rectangle):
	def __init__(self, size):
		super().__init__(size, size)
		
	@Rectangle.width.setter
	def width(self, value):
		self._width=self._height=value
		
	@Rectangle.height.setter
	def height(self, value):
		self._width=self._height=value
	
	
#test
r=Rectangle(10, 25)
print(r)
print(r.area)

s=Square(30)
print(s)
print(s.area)