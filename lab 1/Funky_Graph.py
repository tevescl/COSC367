from search import *
from collections import deque

from itertools import dropwhile

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        # class Arc(namedtuple('Arc', 'tail, head, action, cost')):

        return [Arc(tail_node, tail_node-1, action="1down", cost=1),
                Arc(tail_node, tail_node+2, action="2up", cost=1)]
        
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        if node%10 ==0:
            return True
        else:
            return False 
            
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
        
graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))