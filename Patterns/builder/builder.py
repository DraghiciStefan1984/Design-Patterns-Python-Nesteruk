
class HtmlElement:
	indent_size=2
	
	def __init__(self, name='', text=''):
		self.name=name
		self.text=text
		self.elements=[]
		
	def __str(self, indent):
		lines=[]
		i=' '*(indent*self.indent_size)
		lines.append(f'{i}<{self.name}>')
		
		if self.text:
			i1=' '*((indent+1)*self.indent_size)
			lines.append(f'{i1}{self.text}')
			
		for e in self.elements:
			lines.append(e.__str(indent+1))
			
		lines.append(f'{i}</{self.name}>')
		return '\n'.join(lines)
		
	def __str__(self):
		return self.__str(0)
		
	@staticmethod
	def create(name):
		return HtmlBuilder(name)
		

class HtmlBuilder:
	def __init__(self, root_name):
		self.root_name=root_name
		self.__root=HtmlElement(name=root_name)
	
	#lazy way	
	def add_child(self, child_name, child_text):
		self.__root.elements.append(HtmlElement(child_name, child_text))
		
	#fluent way, permits chaining
	def add_child_fluent(self, child_name, child_text):
		self.__root.elements.append(HtmlElement(child_name, child_text))
		return self
		
	def __str__(self):
		return str(self.__root)


#test
#builder=HtmlBuilder('ul')
builder=HtmlElement.create('ul')
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'hi').add_child_fluent('li', 'aloha')
print(builder)