
"""
interpretations.py testing 
"""
#from interpretations import interpretations

#atoms = {'q', 'p'}
#for i in interpretations(atoms):
    #print(i)

##{'p': False, 'q': False}
##{'p': False, 'q': True}
##{'p': True, 'q': False}
##{'p': True, 'q': True}
    
    
"""
models.py testing 
"""
#from models import models

#knowledge_base = {
    #lambda a, b: a and not b,
    #lambda c: c
#}

#print(models(knowledge_base))

##[{'a': True, 'b': False, 'c': True}]

"""
forward_deduce.py testing 
"""
#from forward_deduce import forward_deduce

#kb = """
#a :- b.
#b.
#"""

#print(", ".join(sorted(forward_deduce(kb))))


#kb = """
#a :- b, c.
#b :- d, e.
#b :- g, e.
#c :- e.
#d.
#e.
#f :- a,
     #g.
#"""

#print(", ".join(sorted(forward_deduce(kb))))
##a, b, c, d, e

"""
forward_deduce.py testing 
"""
from search import *
from top_down import KBGraph, DFSFrontier


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