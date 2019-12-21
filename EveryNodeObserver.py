from Observer import Observer

class EveryNodeObserver(Observer):
	def update(self, subject):
		if subject._state == 1 or subject._state == 2:
			print('EveryNodeObserver: Reacted to the event')