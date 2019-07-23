from abc import ABC


class Expression(ABC):
	pass


class DoubleExpression(Expression):
	def __init__(self, value):
		self.value=value
		

class AdditionExpression(Expression):
	def __init__(self, left, right):
		self.left=left
		self.right=right
		
		
class ExpressionPrinter:
	@staticmethod
	def custom_print(e, buffer):
		if isinstance(e, DoubleExpression):
			buffer.append(str(e.value))
		elif isinstance(e, AdditionExpression):
			buffer.append('(')
			ExpressionPrinter.custom_print(e.left, buffer)
			buffer.append('+')
			ExpressionPrinter.custom_print(e.right, buffer)
			buffer.append(')')
	Expression.custom_print=lambda self, b: ExpressionPrinter.custom_print(self, b)
		
		
#test
e=AdditionExpression(DoubleExpression(1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))
buffer=[]
ExpressionPrinter.custom_print(e, buffer)
print(''.join(buffer))