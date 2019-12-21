from Subject import Subject

class ConcreteSubject(Subject):
	_state: int = None
	_observers = []
	
	def attach(self, observer):
		print('Subject: Attached an observer')
		self._observers.append(observer)

	def detach(self, observer):
		self._observers.remove(observer)

	def notify(self):
		print('Subject: Notifying observers...')
		for observer in self._observers:
			observer.update(self)
	
	def some_business_logic(self):
		print('\nSubject: I`m doing something important')
		self.notify()