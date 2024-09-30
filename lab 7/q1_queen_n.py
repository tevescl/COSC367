"""
Lab 7 question 1 
n-queens puzzle
"""

import itertools

def n_queens_neighbours(state):
    #combinations(iterator, r)

    return sorted(tuple(state[:i] + (state[j],) + state[i+1:j] + (state[i],) + state[j+1:])
        for i, j in itertools.combinations(range(len(state)), 2)
    )