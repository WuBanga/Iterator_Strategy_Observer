from ConcreteSubject import ConcreteSubject
from EveryNodeObserver import EveryNodeObserver
from EvenNodeObserver import EvenNodeObserver
from Graph import Graph
from BFS import BFS
from DFS import DFS


if __name__ == "__main__":
	subject = ConcreteSubject()

	observer_a = EveryNodeObserver()
	subject.attach(observer_a)
	
	observer_b = EvenNodeObserver()
	subject.attach(observer_b)

	
	graph1 = Graph(BFS())
	graph1.add_item([6, 2, 5])
	graph1.add_item([7, 1, 3])
	graph1.add_item([2, 8, 4])
	graph1.add_item([9, 5, 3])
	graph1.add_item([10, 1, 4])
	graph1.add_item([11, 1, 12])
	graph1.add_item([12, 13, 2])
	graph1.add_item([3, 13, 14])
	graph1.add_item([15, 4, 14])
	graph1.add_item([11, 5, 15])
	graph1.add_item([16, 6, 10])
	graph1.add_item([17, 7, 6])
	graph1.add_item([7, 8, 18])
	graph1.add_item([8, 9, 19])
	graph1.add_item([10, 9, 20]) 
	graph1.add_item([17, 20, 11])
	graph1.add_item([16, 12, 18])
	graph1.add_item([17, 13, 19])
	graph1.add_item([14, 20, 18])
	graph1.add_item([15, 16, 19])

	print('Graph: BFS graph traversal')
	graph1.do_some_business_logic(subject)
	print()


	graph2 = Graph(DFS())
	graph2.add_item([6, 2, 5])
	graph2.add_item([7, 1, 3])
	graph2.add_item([2, 8, 4])
	graph2.add_item([9, 5, 3])
	graph2.add_item([10, 1, 4])
	graph2.add_item([11, 1, 12])
	graph2.add_item([12, 13, 2])
	graph2.add_item([3, 13, 14])
	graph2.add_item([15, 4, 14])
	graph2.add_item([11, 5, 15])
	graph2.add_item([16, 6, 10])
	graph2.add_item([17, 7, 6])
	graph2.add_item([7, 8, 18])
	graph2.add_item([8, 9, 19])
	graph2.add_item([10, 9, 20])
	graph2.add_item([17, 20, 11])
	graph2.add_item([16, 12, 18])
	graph2.add_item([17, 13, 19])
	graph2.add_item([14, 20, 18])
	graph2.add_item([15, 16, 19])
	
	print('Graph: DFS graph traversal')
	graph2.do_some_business_logic(subject)
	print()