
class Driver:
	def __init__(self, name, age):
		self.name=name
		self.age=age
		
		
class Car:
	def __init__(self, driver):
		self.driver=driver
		
	def drive(self):
		print(f'The car is being driven by {self.driver.name}.')
		
		
class CarProxy:
	def __init__(self, driver):
		self.driver=driver
		self._car=Car(driver)
		
	def drive(self):
		if self.driver.age>=18:
			self._car.drive()
		else:
			print('Too young to drive.')
		
#test
driver=Driver('John', 35)
#car=Car(driver)
car=CarProxy(driver)
car.drive()