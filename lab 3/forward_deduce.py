import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(kb_str):
    """Takes the string of a knowledge base containing propositional definite 
    clauses and returns a (complete) set of atoms (strings) that can be derived 
    (to be true) from the knowledge base.
    """
    prop_def_clauses = list(clauses(kb_str))
    
    atoms = set()
    
    for head, body in prop_def_clauses:
        #yes <-.
        if not body:
            atoms.add(head)
            
    
    while True:
        new_atoms = set()
        for head, body in prop_def_clauses:
            
            #cond 1 
            if head in atoms:
                continue
            #cond 2
            if all(atom in atoms for atom in body):
                new_atoms.add(head)
                
        if not new_atoms:
            break
        atoms.update(new_atoms)
            
    return atoms
    
## Check each clause in the knowledge base
## if all atoms in body then that head can be added 
            
## If no new atoms were derived, exit the loop
## update atoms set 
            