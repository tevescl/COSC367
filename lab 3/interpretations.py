"""
Takes a non-empty set of atoms and returns the list of all possible interpretations 
for the given atoms.
"""

from itertools import product

def interpretations(atoms):
    """
    return possible interpretation of atoms
    2^n = T F
    #dictionary = {atoms:interpretation T}
    #keys alphabetical order 
    """
    atoms = sorted(atoms)
    all_possible  = list(product([False,True], repeat=(len(atoms))))
    
    interpretations_list = []
    for interepretation in all_possible:
        final = {}
        for index in range(len(atoms)):
            final[atoms[index]] = interepretation[index]
        interpretations_list.append(final)
    return interpretations_list
        