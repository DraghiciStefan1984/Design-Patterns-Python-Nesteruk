from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):
	def start(self, buffer): pass
	def end(self, buffer): pass
	def add_list_item(self, buffer, item): pass
	
	
class MarkdownListStrategy(ListStrategy):
	def add_list_item(self, buffer, item):
		buffer.append(f' * {item}\n')
	
	
class HTMLListStrategy(ListStrategy):
	def start(self, buffer):
		buffer.append('<ul>\n')
		
	def end(self, buffer):
		buffer.append('</ul>\n')
		
	def add_list_item(self, buffer, item):
		buffer.append(f'<li>{item}</li>\n')


class OutputFormat(Enum):
	MARKDOWN=auto()
	HTML=auto()

class TextProcessor:
	def __init__(self, list_strategy=HTMLListStrategy()):
		self.list_strategy=list_strategy
		self.buffer=[]
		
	def append_list(self, items):
		ls=self.list_strategy
		ls.start(self.buffer)
		for item in items:
			ls.add_list_item(self.buffer, item)
		ls.end(self.buffer)
		
	def set_output_format(self, format):
		if format==OutputFormat.MARKDOWN:
			self.list_strategy=MarkdownListStrategy()
		elif format==OutputFormat.HTML:
			self.list_strategy=HTMLListStrategy()
			
	def clear(self):
		self.buffer.clear()
		
	def __str__(self):
		return ''.join(self.buffer)
		
		
#test
items=['fdg','dfdg','fdsd','fsf']
tp=TextProcessor()
tp.set_output_format(OutputFormat.HTML)
tp.append_list(items)
tp.clear()
print(tp)
tp.set_output_format(OutputFormat.MARKDOWN)
tp.append_list(items)
print(tp)