
class Event(list):
	def __call__(self, *args, **kwargs):
		for item in self:
			item(*args, **kwargs)
			
			
class PropertyObservable:
	def __init__(self):
		self.property_changed=Event()
		

class Person(PropertyObservable):
	def __init__(self, age=0):
		super().__init__()
		self._age=age
		
	@property
	def can_vote(self):
		return self._age>=18
		
	@property
	def age(self):
		return self._age
		
	@age.setter
	def age(self, value):
		if self._age==value:
			return
		old_can_vote=self.can_vote
		self._age=value
		self.property_changed('age', value)
		
		if old_can_vote!=self.can_vote:
			self.property_changed('can_vote', self.can_vote)


class TrafficAuthority:
	def __init__(self, person):
		self.person=person
		person.property_changed.append(self.person_changed)
			
	def person_changed(self, name, value):
		if name=='age':
			if value<=16:
				print('Sorry, to young to drive.')
			else:
				print('You can drive.')
				self.person.property_changed.remove(self.person_changed)
		if name=='can_vote':
			print(f'Can vote: {value}')
		
		
#test
p=Person(18)
ta=TrafficAuthority(p)
for age in range(14, 20):
	print(f'Setting age to {age}')
	p.age=age