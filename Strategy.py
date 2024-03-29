from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, graph, start):
        pass