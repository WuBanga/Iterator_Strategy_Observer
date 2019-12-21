from Observer import Observer

class EvenNodeObserver(Observer):
	def update(self, subject):
		if subject._state == 2:
			print('EvenNodeObserver: Reacted to the event')