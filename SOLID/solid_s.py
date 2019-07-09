class Journal:
	def __init__(self):
		self.entries=[]
		self.count=0
		
	def add_entry(self, text):
		self.count+=1
		self.entries.append(f'{self.count}:{text}')
		
	def remove_entry(self, pos):
		del self.entries[pos]
		
	def __str__(self):
		return '\n'.join(self.entries)
		
		
class Persistence:
	@staticmethod
	def save(journal, filename):
		file=open(filename, 'w')
		file.write(str(journal))
		file.close()
		
	@staticmethod
	def load(self, filename):
		pass
		
	@staticmethod
	def load_from_web(self, uri):
		pass
		
		
#test
j=Journal()
j.add_entry('hello')
j.add_entry('hi')
j.add_entry('aloha')
j.add_entry('salut')
Persistence.save(j, 'test.txt')
print(j)