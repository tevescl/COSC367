"""
Lab 7 question 2
n-queens puzzle
return no. of conflicts 
"""


import itertools

def n_queens_cost(state):
    return sum(abs(i - j) == abs(state[i] - state[j])
        for i, j in itertools.combinations(range(len(state)), 2)
    )


print(n_queens_cost((1, 2)))
print(n_queens_cost((1, 3, 2)))

print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))

