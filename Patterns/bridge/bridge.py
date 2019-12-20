from abc import ABC

class Renderer(ABC):
	def render_circle(self, radius):
		pass
		
		
class VectorRenderer(Renderer):
	def render_circle(self, radius):
		print(f'drawing a circle of radius {self.radius}')
		
		
class RasterRenderer(Renderer):
	def render_circle(self, radius):
		print(f'drawing pixels for a circle of radius {self.radius}')
		
		
class Shape:
	def __init__(self, renderer):
		self.renderer=renderer
		
	def draw(self):
		pass
		
	def resize(self, factor):
		pass
		
		
class Circle(Shape):
	def __init__(self, renderer):
		super().__init__(renderer)
		self.radius=radius
		
	def draw(self):
		self.renderer.render_circle(self.radius)
		
	def resize(self, factor):
		self.radius*=factor
		
		
#test
raster=RasterRenderer()
vector=VectorRenderer()
circle1=Circle(vector, 5)
circle1.draw()
circle2=Circle(raster, 8)
circle2.draw()