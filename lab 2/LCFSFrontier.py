from search import *
from math import sqrt
import heapq

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        #IMPLEMENTED 
        return node  in self.goal_nodes
    
    
    def outgoing_arcs(self, tail):
        """
        In the outgoing_arcs method, we calculate the distance between the tail node and every other node in
        the graph and create an outgoing arc to each node that is within the given radius. The arcs represent 
        the possible actions the agent can take from the current node (tail) to reach other neighboring nodes
        (head).
        """
        #IMPLEMENTED 
        arcs = []
        x1, y1 = self.location[tail] # tail = starting node
        
        for head, (x2, y2) in self.location.items(): #iterate through edge list 
            
            if tail != head: # if tail not the goal/head
                
                # euclidean distance = between the start node (x1,y1) and iterated/current node(x2,y2)
                euclidean_distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
                
                #only within radius of each othe if :
                if euclidean_distance <= self.radius:
                    
                    #refer to search.py for layout ... setting attributes 
                    #cost could euclidean, heuristic etc.
                    arcs.append(Arc(tail=tail, head=head, action=f"{tail}->{head}", cost=euclidean_distance))
        
        arcs.sort(key=lambda arc: arc.cost)  # Sort arcs in alphabetical order of head nodes
        return arcs        
    
class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []  # priority queue
        self.visited = {}  # Mapping of nodes to entries in the queue
        #visited = {
                    #path0: (17, 0, path0),
                    #path1: (7, 1, path1),
                    #path2: (11, 2, path2)
                #}
                
        self._counter = 0  # to make the priority queue stable
        #counter is used when multiple paths have the same costs 
        

    def add(self, path):
        cost = sum(arc.cost for arc in path)  # total accumulated cost of the path
        
        entry = [cost, self._counter, path]
        self._counter += 1
        self.visited[path] = entry
        heapq.heappush(self.container, entry)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.container:
            raise StopIteration
        _, _, path = heapq.heappop(self.container)
        del self.visited[path]
        return path


def main ():
    """Tests"""
      
      
    #TEST1
    frontier = LCFSFrontier()
    frontier.add((Arc(None, None, None, 17),))
    frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
    frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))
    
    for path in frontier:
        print(path)    
            
    #TEST2
    graph = LocationGraph(
           location={'A': (25, 7),
                     'B': (1, 7),
                     'C': (13, 2),
                     'D': (37, 2)},
           radius=15,
           starting_nodes=['B'],
           goal_nodes={'D'}
    )
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)       
    
     ##TEST3 
    graph = ExplicitGraph(nodes=set('ABCD'),
                          edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                     ('B', 'C', 3), ('C', 'D', 1)],
                          starting_nodes=['A'],
                          goal_nodes={'D'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    #test 4
    
    graph = LocationGraph(
        location={'A': (0, 0),
                  'B': (3, 0),
                  'C': (3, 4),
                  'D': (7, 0),},
        radius = 5,
        starting_nodes=['A'],
        goal_nodes={'C'}
    )
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)    
     
     
  
if __name__ == "__main__":
    main()
    
