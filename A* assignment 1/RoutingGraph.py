from search import *
import math

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.map = [list(line) for line in map_str.strip().split('\n')]
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.agents = {}#key = location, value: fuel capacity 
        self.goals = set()
        self.portals = []
        
        for row_num, row in enumerate(self.map):
            for col_num, cell_char in enumerate(row):
                if cell_char == 'G':
                    self.goals.add((row_num, col_num))
                elif cell_char == 'S':#dont need fuel
                    self.agents[(row_num, col_num)] = math.inf
                elif cell_char.isdigit():#agent
                    self.agents[(row_num, col_num)] = int(cell_char)
                elif cell_char == 'P':
                    self.portals.append((row_num, col_num))
        
        
    def starting_nodes(self):
        result = []
        for (row_num, col_num), fuel in self.agents.items():
            result.append((row_num, col_num, fuel))
        return result

    def is_goal(self, node):
        row_num, col_num, _ = node #dont need last val
        return (row_num, col_num) in self.goals # return bool if in goal set 
    
    def outgoing_arcs(self, tail_node):
        row_num, col_num, fuel = tail_node
        arcs = []
        
        #(direction,x,y,cost)
        movements = [
            ('N', -1, 0, 5), ('NE', -1, 1, 7), ('E', 0, 1, 5), ('SE', 1, 1, 7),
            ('S', 1, 0, 5), ('SW', 1, -1, 7), ('W', 0, -1, 5), ('NW', -1, -1, 7)
        ]
        
        for action, row_pos, col_pos, cost in movements:
            new_row, new_col = row_num + row_pos, col_num + col_pos
            #loops through movements until it finds a valid one 
            if self.map[new_row][new_col] not in '+-|X' and fuel > 0: 
                new_fuel = fuel - 1
                arcs.append(Arc(tail_node, (new_row, new_col, new_fuel), action, cost))
        
        if self.map[row_num][col_num] == 'F' and fuel < 9:
            arcs.append(Arc(tail_node, (row_num, col_num, 9), 'Fuel up', 15))
        
        if self.map[row_num][col_num] == 'P':
            for port_posr, port_posc in self.portals:
                if (port_posr, port_posc) != (row_num, col_num):
                    arcs.append(Arc(tail_node, (port_posr, port_posc, fuel), f'Teleport to ({port_posr}, {port_posc})', 10))
        
        return arcs




