from student_answer import LocationGraph

graph = LocationGraph(
    location={'A': (0, 0),
              'B': (3, 0),
              'C': (3, 4),
              'D': (7, 0),},
    radius = 5,
    starting_nodes=['A'],
    goal_nodes={'C'}
)

for node in graph.starting_nodes():
    print(node)

print()

for arc in graph.outgoing_arcs('A'):
    print(arc)

print()

for arc in graph.outgoing_arcs('B'):
    print(arc)

print()

for arc in graph.outgoing_arcs('C'):
    print(arc)