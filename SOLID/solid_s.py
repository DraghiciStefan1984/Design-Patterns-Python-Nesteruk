class Journal:
	def __init__(self):
		self.entries=[]
		self.count=0
		
	def add_entry(self, text):
		self.count+=1
		self.entries.append(f'{self.count}:{text}')
		
	def remove_entry(self, position):
		self.count-=1
		del self.entries[position]
		
	def __str__(self):
		return '\n'.join(self.entries)


class PersistenceManager:
	@staticmethod
	def save_to_file(journal, filename):
		file=open(filename, 'w')
		file.write(str(journal))
		file.close()

	@staticmethod
	def load(filename):
		pass
	
	@staticmethod
	def load_from_web(uri):
		pass		
		
		
#test
j=Journal()
j.add_entry('first entry')
j.add_entry('second entry')
j.add_entry('third entry')
print(j)
#j.remove_entry(1)
#print(j)

file=r'D:\Cursuri\Design-Patterns-Python-Nesteruk\SOLID\journal.txt'
PersistenceManager.save_to_file(j, file)