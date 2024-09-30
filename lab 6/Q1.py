#tree for perfection information game 
#pseudocode provided in the lectures assume that the top node is a max

import math

def max_value(tree):
    if isinstance(tree, int):  
        return tree
    
    v = -math.inf
    for subtree in tree:
        if isinstance(subtree, int):
            v = max(v, subtree)
        else:
            v = max(v, min_value(subtree))  
    
    return v


def min_value(tree):
    if isinstance(tree, int): 
        return tree
    
    v = math.inf
    for subtree in tree:
        if isinstance(subtree, int):
            v = min(v, subtree)
        else:
            v = min(v, max_value(subtree))  
    
    return v

game_tree = 3

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))




####
game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))