from search import Arc, Graph
from math import sqrt

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
        
        arcs.sort(key=lambda arc: arc.head)  # Sort arcs in alphabetical order of head nodes
        return arcs        
        
        



def main ():
    """Tests"""
    
    #TEST 1 
    
    graph = LocationGraph(
        location={'A': (0, 0),
                  'B': (3, 0),
                  'C': (3, 4),
                  'D': (7, 0),},
        radius = 5,
        starting_nodes=['A'],
        goal_nodes={'C'}
    )
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    print()
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    print()
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)    
    
    
    
    
if __name__ == "__main__":
    main()
    