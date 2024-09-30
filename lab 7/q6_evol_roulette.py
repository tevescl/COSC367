"""
Lab 7 question 6
evolutionary computation

returns an individual from the population
"""

def roulette_wheel_select(population, fitness, r):
    total_fitness = sum(fitness(individual) for individual in population)
    
    cumulative_distribution = []
    total = 0
    
    for individual in population:
        individual_fitness = fitness(individual)
        total += individual_fitness
        cumulative_distribution.append(total)
    
    selection_value = r * total_fitness

    
    for i, cumulative in enumerate(cumulative_distribution):
        if selection_value < cumulative:
            return population[i]

    return population[-1]


population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))