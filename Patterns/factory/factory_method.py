from enum import Enum

class CoordinateSystem(Enum):
	CARTESIAN=1
	POLAR=2


class Point:
'''
	def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
		if system==CoordinateSystem.CARTESIAN:
			self.x=a
			self.y=b
		elif system==CoordinateSystem.POLAR:
			self.x=a*cos(b)
			self.y=a*sin(b)
'''
	def __init__(self, x, y):
		self.x=x
		self.y=y

	@staticmethod
	def new_cartesian_point(x, y):
		return Point(x, y)

	@staticmethod
	def new_polar_point(rho, theta):
		return Point(rho*cos(theta), rho*sin(theta))

	def __str__(self):
		return f'x:{self.x}, y:{self.y}'


#test
p1=Point(23, 55)
p2=Point.new_cartesian_point(12, 15)
p3=Point.new_polar_point(12, 13)
print(p1)
print(p2)
print(p3)