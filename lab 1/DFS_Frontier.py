from search import *

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        """take an arc tuple named path, must iterate its """
            
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        
        #STOPS THE SEARCH WHEN ALL THE SOLUTIONS ARE FOUND
        #NOTE THAT IF THERE ARE INFITE NODES IN A SECTION OF THE GRAPH
        #IT WILL HAVE INFINITE LOOP
        #BUT THESE WILL NOT BE INCLUDED IN THE TEST CASES IN THE LAB
        #WILL COVER PRUNING LATER ON TO SOLVE THIS 
        
        while len(self.container) > 0:
            yield self.container.pop()
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container[-1]
        else:
            raise StopIteration   # don't change this one

def main():
    # Example 1
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    # Example 2
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)


if __name__ == "__main__":
    main()
