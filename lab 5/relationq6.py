from csp import Relation

var_domains = {var: {-1, 0, 1} for var in 'abcd'}

constraints = [
    lambda a, b: a == abs(b),
    lambda c, d: c > d,
    lambda a, b, c: a * b > c + 1
]

relations = [
    ### COMPLETE ###
    
    Relation(
        header=['a', 'b'],
        tuples={(a, b) for a in var_domains['a'] for b in var_domains['b'] if a == abs(b)}
    ),
    Relation(
        header=['c', 'd'],
        tuples={(c, d) for c in var_domains['c'] for d in var_domains['d'] if c > d}
    ),
    Relation(
        header=['a', 'b', 'c'],
        tuples={(a, b, c) for a in var_domains['a'] for b in var_domains['b'] for c in var_domains['c'] if a * b > c + 1}
    )
]

relations_after_elimination = [
    ### COMPLETE ###
    
    Relation(
        header=['b', 'c'],
        tuples={(b, c) for b in var_domains['b'] for c in var_domains['c']
                if any(a * b > c + 1 for a in var_domains['a'])}
    ),
    Relation(
        header=['c', 'd'],
        tuples={(c, d) for c in var_domains['c'] for d in var_domains['d'] 
                if (c > d )}
    )
]

print(len(relations))

print(all(type(r) is Relation for r in relations))
print(sorted(relations_after_elimination)[1].header)
print(sorted(sorted(relations_after_elimination)[0].tuples))
