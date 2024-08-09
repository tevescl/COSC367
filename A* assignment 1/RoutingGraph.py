from search import *
import math
#draw graph of each agent


class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.map = [list(line) for line in map_str.strip().split('\n')]
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        print (self.rows,self.cols)
        self.agents = {}
        self.goals = set()
        self.portals = []
        
        for r, row in enumerate(self.map):
            print (r,row)
            for c, char in enumerate(row):
                if char == 'G':
                    self.goals.add((r, c))
                elif char == 'S':
                    self.agents[(r, c)] = math.inf
                elif char.isdigit():
                    self.agents[(r, c)] = int(char)
                elif char == 'P':
                    self.portals.append((r, c))
    
    def starting_nodes(self):
        return [(r, c, fuel) for (r, c), fuel in self.agents.items()]
    
    def is_goal(self, node):
        row, col, _ = node
        return (row, col) in self.goals
    
    def outgoing_arcs(self, tail_node):
        row, col, fuel = tail_node
        arcs = []

        # would need to adjust this depending on size of graph
        movements = [
            ('N', -1, 0, 5), ('NE', -1, 1, 7), ('E', 0, 1, 5), ('SE', 1, 1, 7),
            ('S', 1, 0, 5), ('SW', 1, -1, 7), ('W', 0, -1, 5), ('NW', -1, -1, 7)
        ]
        
        for action, dr, dc, cost in movements:
            new_row, new_col = row + dr, col + dc
            if self.map[new_row][new_col] not in '+-|X' and fuel > 0:
                new_fuel = fuel - 1
                arcs.append(Arc(tail_node, (new_row, new_col, new_fuel), action, cost))
        
        if self.map[row][col] == 'F' and fuel < 9:
            arcs.append(Arc(tail_node, (row, col, 9), 'Fuel up', 15))
        
        if self.map[row][col] == 'P':
            for pr, pc in self.portals:
                if (pr, pc) != (row, col):
                    arcs.append(Arc(tail_node, (pr, pc, fuel), f'Teleport to ({pr}, {pc})', 10))
        
        return arcs
