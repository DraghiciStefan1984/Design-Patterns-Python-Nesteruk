

class Bitmap:
	def __init__(self, filename):
		self.filename=filename
		print(f'loading from {self.filename}.')
		
	def draw(self):
		print('drawing image')
		
		
class LazyBitmap:
	def __init__(self, filename):
		self.filename=filename
		self._bitmap=None
		
	def draw(self):
		if not self._bitmap:
			self._bitmap=Bitmap(self.filename)
		self._bitmap.draw()
		
		
def draw_image(image):
	print('about to draw image')
	image.draw()
	print('done drawing image')
		
#test
b=LazyBitmap('test.jpg')