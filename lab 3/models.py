# import any module as necessary
from interpretations import interpretations

def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """
    
    return {atom for atom in formula.__code__.co_varnames}
    
def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)


def models(knowledge_base):
    """
    takes a knowledge base and return models
    1. 
    """
    all_atoms = set()
    for formula in knowledge_base:
        all_atoms.update (atoms(formula))
    
    all_interpretations = interpretations(all_atoms)
    #print (all_interpretations)
    
    all_models = [ 
        #contains all possible interpretations of the atoms in the knowledge base.
        interpretation for interpretation in all_interpretations
        #Condition Filtering with if:
        #all function returns True if all elements in the given iterable are True. 
        if all (value(knowledge, interpretation) for knowledge in knowledge_base)
        ]
    
    
            
    return all_models
        