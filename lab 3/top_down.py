import re
from search import *


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


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return [self.query]
        
    def is_goal(self, node):
        # has no body
        if node == []:
            return True  
        else:
            return False

    def outgoing_arcs(self, tail_node):
        arcs = []
        tail = list(tail_node)

        for clause in self.clauses:
            if clause[0] == tail[0]:
                if len(tail) > 1 :
                    head = tail[1:]
                else: 
                    head = []
                
                for body in clause[1]:
                    head.insert(0, body)

                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), 1))

        return arcs 


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        """take an arc tuple named path, must iterate its """
            
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        
        #STOPS THE SEARCH WHEN ALL THE SOLUTIONS ARE FOUND
        #NOTE THAT IF THERE ARE INFITE NODES IN A SECTION OF THE GRAPH
        #IT WILL HAVE INFINITE LOOP
        #BUT THESE WILL NOT BE INCLUDED IN THE TEST CASES IN THE LAB
        #WILL COVER PRUNING LATER ON TO SOLVE THIS 
        
        while len(self.container) > 0:
            yield self.container.pop()
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container[-1]
        else:
            raise StopIteration   # don't change this one



#Sample usage for testing
if __name__ == "__main__":
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    query = {'c'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")