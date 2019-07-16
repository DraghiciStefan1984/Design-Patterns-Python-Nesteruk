import unittest
from composite_command import  BankAccount, BankAccountCommand, CompositeBankAccountCommand


class TestSuite(unittest.TestCase):
	def test_composite_deposit(self):
		ba=BankAccount()
		deposit1=BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
		deposit2=BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
		composite=CompositeBankAccountCommand([deposit1, deposit2])
		composite.invoke()
		print(ba)
		composite.undo()
		print(ba)
		
	def test_transfer_fail(self):
		ba1=BankAccount(100)
		ba2=BankAccount()
		amount=100
		withdraw=BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
		deposit=BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)
		transfer=CompositeBankAccountCommand([withdraw, deposit])
		transfer.invoke()
		print(f'ba1: {ba1}')
		print(f'ba2: {ba2}')
		transfer.undo()
		
#test
if __name__=='__main__':
	unittest.main()