from enum import Enum
from math import *

'''
class CoordinateSystem(Enum):
	CARTESIAN=1
	POLAR=2	
'''

class Point:
	def __init__(self, x=0, y=0):
		self.x=x
		self.y=y
		
	def __str__(self):
		return f"({self.x}, {self.y})"
		

class PointFactory:
	@staticmethod
	def new_cartesian_point(x, y):
		return Point(x, y)
		
	@staticmethod
	def new_polar_point(rho, theta):
		return Point(rho*cos(theta), rho*sin(theta))
	
	
#test
p1=Point(8, 5)
p2=PointFactory.new_polar_point(8, 5)

print(p1)
print(p2)