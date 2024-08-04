from search import *
from collections import deque
class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""
    
    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container =  deque()


    def add(self, path):
        """take an arc tuple named path, must iterate its """
            
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        while len(self.container) > 0:
            yield self.container.popleft()
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration   # don't change this one
    