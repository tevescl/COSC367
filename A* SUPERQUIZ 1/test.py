from student_answer import RoutingGraph, AStarFrontier
from search import *

########## TEST1 ##########

map_str = """\
+-------+
|   G   |
|       |
|   S   |
+-------+
"""
map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_actions(solution)
#Actions:
  #N,
  #N.
#Total cost: 10

########## TEST2 ##########

#map_str = """\
#+-------+
#|  GG   |
#|S    G |
#|  S    |
#+-------+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##Actions:
  ##N,
  ##N.
##Total cost: 10

########## TEST3 ##########
#map_str = """\
#+-------+
#|     XG|
#|X XXX  |
#| S     |
#+-------+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##Actions:
  ##E,
  ##E,
  ##E,
  ##NE,
  ##NE.
##Total cost: 29

########## TEST4 ##########

#map_str = """\
#+-------+
#|  F  X |
#|X XXXXG|
#| 3     |
#+-------+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##Actions:
  ##N,
  ##NE,
  ##Fuel up,
  ##SW,
  ##SE,
  ##E,
  ##E,
  ##E,
  ##NE.
##Total cost: 63
########## TEST5 ##########

#map_str = """\
#+--+
#|GS|
#+--+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##Actions:
  ##W.
##Total cost: 5

########## TEST6 ##########

#map_str = """\
#+---+
#|GF2|
#+---+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##Actions:
  ##W,
  ##W.
##Total cost: 10

########## TEST6 ##########

#map_str = """\
#+----+
#| S  |
#| SX |
#|GX G|
#+----+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##Actions:
  ##SW.
##Total cost: 7

########## TEST7 ##########

#map_str = """\
#+---------+
#|         |
#|    G    |
#|         |
#+---------+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
##There is no solution!