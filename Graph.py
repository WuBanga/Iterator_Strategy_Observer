from collections.abc import Iterable
from GraphIterator import GraphIterator

class Graph(Iterable):
	def __init__(self, strategy, collection = []):
		self._collection = collection
		self._strategy = strategy

	def __iter__(self):
		return GraphIterator(self._collection)

	def add_item(self, item):
		self._collection.append(sorted(map(lambda x: x - 1, item)))
	
	@property
	def strategy(self):
		return self._strategy

	@strategy.setter
	def strategy(self, strategy):
		self._strategy = strategy
	
	def do_some_business_logic(self, subject):
		print('Graph: graph traversal using the strategy')
		for item in self._strategy.do_algorithm(self._collection, 0, subject):
			# if item == 5:
			# 	return
			print(item)