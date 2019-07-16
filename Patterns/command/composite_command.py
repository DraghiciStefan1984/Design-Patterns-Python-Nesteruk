from abc import ABC
from enum import Enum


class BankAccount:
	OVERDRAFT_LIMIT=-500
	
	def __init__(self, balance=0):
		self.balance=balance
		
	def deposit(self, amount):
		self.balance+=amount
		print(f'Deposited {amount}, balance={self.balance}')
		
	def withdraw(self, amount):
		if self.balance-amount>=BankAccount.OVERDRAFT_LIMIT:
			self.balance-=amount
			print(f'Withdrew {amount}, balance={self.balance}')
			return True
		return False
			
	def __str__(self):
		return f'Balance={self.balance}'
		
		
class Command(ABC):
	def invoke(self):
		pass
		
	def undo(self):
		pass
		
		
class BankAccountCommand(Command):
	class Action(Enum):
		DEPOSIT=0
		WITHDRAW=1
		
	def __init__(self, account, action, amount):
		self.account=account
		self.action=action
		self.amount=amount
		self.success=None
		
	def invoke(self):
		if self.action==self.Action.DEPOSIT:
			self.account.deposit(self.amount)
			self.success=True
		elif self.action==self.Action.WITHDRAW:
			self.success=self.account.withdraw(self.amount)
			
	def undo(self):
		if self.success:
			if self.action==self.Action.DEPOSIT:
				self.account.withdraw(self.amount)
			elif self.action==self.Action.WITHDRAW:
				self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):
	def __init__(self, items=[]):
		super().__init__()
		for i in items:
			self.append(i)
			
	def invoke(self):
		for x in self:
			x.invoke()
			
	def undo(self):
		for x in reversed(self):
			x.undo()
			
			
#test
ba=BankAccount()
cmd=BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 180)
cmd.invoke()
print(ba)
cmd.undo()
print(ba)