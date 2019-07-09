from enum import Enum
from abc import ABC, abstractmethod


class Printer(ABC):
	@abstractmethod
	def printDoc(self, doc):
		pass
		
		
class Scanner(ABC):
	@abstractmethod
	def scanDoc(self, doc):
		pass
		
		
class Fax(ABC):
	@abstractmethod
	def faxDoc(self, doc):
		pass
	
	
class MultiPrinter(Printer, Scanner, Fax):
	def printDoc(self, doc):
		print('print doc')
		
	def scanDoc(self, doc):
		print('scan doc')
		
	def faxDoc(self, doc):
		print('fax doc')
		

class OldPrinter(Printer):
	def printDoc(self, doc):
		print('old printer print doc')
		
		
class FaxMachine(Fax):
	def faxDoc(self, doc):
		print('fax machine fax doc')
	
#test
