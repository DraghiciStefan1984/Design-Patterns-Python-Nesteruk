
class GraphicObject:
	def __init__(self, color=None):
		self.color=color
		self.children=[]
		self._name='Group'
		
	@property
	def name(self):
		return self._name
		
	@name.setter
	def name(self, value):
		self._name=value
		
	def _print(self, items, depth):
		items.append('*'*depth)
		if self.color:
			items.append(self.color)
		items.append(f'{self.name}\n')
		for child in self.children:
			child._print(items, depth+1)
			
	def __str__(self):
		items=[]
		self._print(items, 0)
		return ''.join(items)
		
		
class Circle(GraphicObject):
	@property
	def name(self):
		return 'Circle'


class Square(GraphicObject):
	@property
	def name(self):
		return 'Square'
		

#test
drawing=GraphicObject()
drawing.name='Drawing'
drawing.children.append(Square('red'))
drawing.children.append(Square('blue'))
drawing.children.append(Circle('yellow'))
drawing.children.append(Circle('green'))

print(drawing)