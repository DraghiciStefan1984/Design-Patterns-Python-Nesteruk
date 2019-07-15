
class FileWithLogging:
	def __init__(self, file):
		self.file=file
		
	def write_lines(self, string):
		self.file.write_lines(string)
		print(f'wrote: {len(strings)} lines.')
		
	def __getattr__(self, item):
		return getattr(self.__dict__['file'], item)
		
	def __setattr__(self, item):
		if key=='file':
			self.__dict__[key]=value
		else:
			setattr(self.__dict__['file'], key)
			
	def __delattr__(self, item):
		delattr(self.__dict__['file'], item)
		
	def __iter__(self):
		return self.file.__iter__()
		
	def __next__(self):
		self.file.__next__()
		
		
#test
file=FileWithLogging(open('hello.txt', 'w'))
file.write_lines(['hello', 'lume'])
file.write('test')
file.close()