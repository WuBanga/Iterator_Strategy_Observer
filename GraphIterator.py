from collections.abc import Iterator

class GraphIterator(Iterator):
	_position = None

	def __init__(self, collection):
		self.collection = collection
		self._position = 0

	def __next__(self):
		try:
			value = self.collection[self._position]
			self._position += 1
		except IndexError:
			raise StopIteration()

		return value