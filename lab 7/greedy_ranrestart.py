"""
Lab 7 question 4
greedy_descent_with_random_restart

print the list of states it goes through 
"""
import itertools

def n_queens_neighbours(state):
    #combinations(iterator, r)

    return sorted(tuple(state[:i] + (state[j],) + state[i+1:j] + (state[i],) + state[j+1:])
        for i, j in itertools.combinations(range(len(state)), 2)
    )

def n_queens_cost(state):
    return sum(abs(i - j) == abs(state[i] - state[j])
        for i, j in itertools.combinations(range(len(state)), 2)
    )

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

def greedy_descent_with_random_restart(random_state, neighbours, cost) :
    while True:
        current = random_state()
        
        states = greedy_descent(current, neighbours, cost)
        
        for state in states:
            print(state)
        
        if cost(states[-1]) == 0:
            break
        else:
            print("RESTART")    
            
            
#import random

#N = 6
#random.seed(0)

#def random_state():
    #return tuple(random.sample(range(1,N+1), N))   

#greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)