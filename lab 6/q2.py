import math

def max_action_value(tree):
    if isinstance(tree, int):  
        return None, tree
    
    alpha = -math.inf

    best_action = None
    
    for i, subtree in enumerate(tree):
        _, value = min_action_value(subtree)  
        if value > alpha:
            alpha = value
            best_action = i
    
    return best_action, alpha


def min_action_value(tree):
    if isinstance(tree, int):  
        return None, tree
    
    beta = math.inf
    best_action = None
    
    for i, subtree in enumerate(tree):
        _, value = max_action_value(subtree) 
        if value < beta:
            beta = value
            best_action = i
    
    return best_action, beta



game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)