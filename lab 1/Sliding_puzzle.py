from search import *
from collections import deque
import copy

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        found = False
        # Find i and j such that state[i][j] == BLANK
          
        for row in range(n):
            for column in range(n):
                if state[row][column] == BLANK:
                    i,j = row,column
                    found = True
                    break
            if found:
                break
                    
        
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            # COMPLETE (repeat the same pattern with some modifications)
            action = "Move {} left".format(state[i][j+1]) # or blank goes right
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))            
            
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        
        n = len(state)
        expected_value = 1
        
        # Check the first element
        if state[0][0] != ' ':
            return False
        
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # Skip the first element since it's blank
                
                if state[i][j] == ' ':
                    return False  # Blank should only be at [0][0]
                
                if state[i][j] != expected_value:
                    return False
                
                expected_value += 1
        
        return True
        

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
