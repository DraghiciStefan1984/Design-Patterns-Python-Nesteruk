class GraphicObject:
	def __init__(self, color=None):
		self.color=color
		self.children=[]
		self.__name='group'
		
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self, value):
		self.__name=value
		
	def __print(self, items, depth):
		items.append('*'*depth)
		if self.color:
			items.append(self.color)
		items.append(f'{self.name}\n')
		for child in self.children:
			child.__print(items, depth+1)
			
	def __str__(self):
		items=[]
		self.__print(items, 0)
		return ''.join(items)
		
		
class Circle(GraphicObject):
	@propoerty
	def name(self):
		return 'Circle'
		
		
class Square(GraphicObject):
	@propoerty
	def name(self):
		return 'Square'
		
		
#test
drawing=GraphicObject()
drawing.name='Drawing'
drawing.children.append(Square('Red'))
drawing.children.append(Circle('Yellow'))

group=GraphicObject()
group.children.append(Circle('Blue'))
group.children.append(Square('Green'))

drawing.children.append(group)