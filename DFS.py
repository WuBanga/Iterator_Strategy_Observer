from Strategy import Strategy

class DFS(Strategy):    
	def do_algorithm(self, graph, start, subject):
		visited, stack = set(), [start]
		while stack:
			vertex = stack.pop()
			if vertex not in visited:
				if vertex % 2 == 0:
					subject._state = 2
					subject.some_business_logic()
				else:
					subject._state = 1
					subject.some_business_logic()
				
				print('Before yield')
				yield vertex
				visited.add(vertex)
				stack.extend(sorted(list(set(graph[vertex]) - visited), 
								reverse=True))

		return