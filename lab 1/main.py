from search import *
from Sliding_puzzle import SlidingPuzzleGraph,BFSFrontier



graph = SlidingPuzzleGraph([[1, 2, 5],
                            [3, 4, 8],
                            [6, 7, ' ']])

solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))