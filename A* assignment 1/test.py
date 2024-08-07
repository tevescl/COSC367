
from RoutingGraph import RoutingGraph
import math

map_str = """\
+-------+
|  9  XG|
|X XXX P|
| S  0FG|
|XX P XX|
+-------+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at starting states:")
for s in sorted(graph.starting_nodes()):
    print(s)
    for arc in graph.outgoing_arcs(s):
        print ("  " + str(arc))

node = (1,1,5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (1,7,2)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))
    
node = (3, 7, 0)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 7, math.inf)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 6, 5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3, 6, 9)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (2, 7, 4)  # at a location with a portal
print("\nOutgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))
    
    
    #Starting nodes: [(1, 3, 9), (3, 2, inf), (3, 5, 0)]
    #Outgoing arcs (available actions) at starting states:
    #(1, 3, 9)
      #Arc(tail=(1, 3, 9), head=(1, 4, 8), action='E', cost=5)
      #Arc(tail=(1, 3, 9), head=(2, 2, 8), action='SW', cost=7)
      #Arc(tail=(1, 3, 9), head=(1, 2, 8), action='W', cost=5)
    #(3, 2, inf)
      #Arc(tail=(3, 2, inf), head=(2, 2, inf), action='N', cost=5)
      #Arc(tail=(3, 2, inf), head=(3, 3, inf), action='E', cost=5)
      #Arc(tail=(3, 2, inf), head=(4, 3, inf), action='SE', cost=7)
      #Arc(tail=(3, 2, inf), head=(3, 1, inf), action='W', cost=5)
    #(3, 5, 0)
    
    #Is (1, 1, 5) goal? False
    #Outgoing arcs (available actions) at (1, 1, 5):
      #Arc(tail=(1, 1, 5), head=(1, 2, 4), action='E', cost=5)
      #Arc(tail=(1, 1, 5), head=(2, 2, 4), action='SE', cost=7)
    
    #Is (1, 7, 2) goal? True
    #Outgoing arcs (available actions) at (1, 7, 2):
      #Arc(tail=(1, 7, 2), head=(2, 7, 1), action='S', cost=5)
      #Arc(tail=(1, 7, 2), head=(2, 6, 1), action='SW', cost=7)
    
    #Is (3, 7, 0) goal? True
    
    #Is (3, 7, inf) goal? True
    #Is (3, 6, 5) goal? False
    #Outgoing arcs (available actions) at (3, 6, 5):
      #Arc(tail=(3, 6, 5), head=(2, 6, 4), action='N', cost=5)
      #Arc(tail=(3, 6, 5), head=(2, 7, 4), action='NE', cost=7)
      #Arc(tail=(3, 6, 5), head=(3, 7, 4), action='E', cost=5)
      #Arc(tail=(3, 6, 5), head=(4, 5, 4), action='SW', cost=7)
      #Arc(tail=(3, 6, 5), head=(3, 5, 4), action='W', cost=5)
      #Arc(tail=(3, 6, 5), head=(3, 6, 9), action='Fuel up', cost=15)
    
    #Is (3, 6, 9) goal? False
    #Outgoing arcs (available actions) at (3, 6, 9):
      #Arc(tail=(3, 6, 9), head=(2, 6, 8), action='N', cost=5)
      #Arc(tail=(3, 6, 9), head=(2, 7, 8), action='NE', cost=7)
      #Arc(tail=(3, 6, 9), head=(3, 7, 8), action='E', cost=5)
      #Arc(tail=(3, 6, 9), head=(4, 5, 8), action='SW', cost=7)
      #Arc(tail=(3, 6, 9), head=(3, 5, 8), action='W', cost=5)
    
    #Outgoing arcs (available actions) at (2, 7, 4):
      #Arc(tail=(2, 7, 4), head=(1, 7, 3), action='N', cost=5)
      #Arc(tail=(2, 7, 4), head=(3, 7, 3), action='S', cost=5)
      #Arc(tail=(2, 7, 4), head=(3, 6, 3), action='SW', cost=7)
      #Arc(tail=(2, 7, 4), head=(2, 6, 3), action='W', cost=5)
      #Arc(tail=(2, 7, 4), head=(4, 4, 4), action='Teleport to (4, 4)', cost=10)    