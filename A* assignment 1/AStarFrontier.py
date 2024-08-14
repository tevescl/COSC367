from search import *
import math
import heapq
from RoutingGraph import RoutingGraph

class AStarFrontier(RoutingGraph):
    def __init__(self, graph):
        self.graph = graph
        self.priority_queue = []  
        self.node_to_entry = {}    
        self.removed = 'REMOVED'  
        self.visited = set()  
        

    def add(self, path):
        node = path[-1].head
        if node in self.visited:
            return

        cost = 0
        for arc in path:
            cost += arc.cost
    
        cost += self.graph.estimated_cost_to_goal(path[-1].head)

        if node in self.node_to_entry:
            old_entry = self.node_to_entry[node]
            if old_entry[0] <= cost:
                return
            self.remove(node)

        queue_item = (cost, path)
        self.node_to_entry[node] = queue_item
        heapq.heappush(self.priority_queue, queue_item)

    def remove(self, node):
        self.node_to_entry[node] = (self.removed, None)

    def __iter__(self):
        while self.priority_queue:
            while self.priority_queue:
                cost, path = heapq.heappop(self.priority_queue)
                if path is not None:
                    break

            node = path[-1].head
            if node not in self.visited:
                self.visited.add(node)
                yield path


