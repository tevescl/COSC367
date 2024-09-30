"""
Lab 7 question 3
greedy_descent
return the list of states it goes through 
"""
def greedy_descent(initial_state, neighbours, cost):
    states = [initial_state]
    current = initial_state
    
    while True:
        neighbour_states = neighbours(current)
        if not neighbour_states:
            break        
        
        next_state = min(neighbour_states, key=cost)
        
        if cost(next_state) < cost(current):
            states.append(next_state)
            current = next_state
        else:
            break
    
    return states




def cost(x):
    return -x**2

def neighbours(x):
    return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
    print(state)