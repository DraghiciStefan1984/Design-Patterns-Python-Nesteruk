class DoubleExpression:
	def __init__(self, value):
		self.value=value
		
	def custom_print(self, buffer):
		buffer.append(str(self.value))
		
	def eval(self):
		return self.value
		

class AdditionExpression:
	def __init__(self, left, right):
		self.left=left
		self.right=right
		
	def custom_print(self, buffer):
		buffer.append('(')
		self.left.custom_print(buffer)
		buffer.append('+')
		self.right.custom_print(buffer)
		buffer.append(')')
		
	def eval(self):
		return self.left.eval()+self.right.eval()
		
#test
e=AdditionExpression(DoubleExpression(1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))
buffer=[]
e.custom_print(buffer)
print(''.join(buffer), '=', e.eval())