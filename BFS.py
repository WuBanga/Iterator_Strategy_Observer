from Strategy import Strategy

class BFS(Strategy):
	def do_algorithm(self, graph, start, subject):
		visited, queue = set(), [start]
		while queue:
			node = queue.pop(0)
			if node not in visited:
				if node % 2 == 0:
					subject._state = 2
					subject.some_business_logic()
				else:
					subject._state = 1
					subject.some_business_logic()
				
				print('Before yield')
				yield node
				visited.add(node)
				for item in graph[node]:
					if item not in visited:
						queue.append(item)
		return