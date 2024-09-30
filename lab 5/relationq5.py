from csp import Relation

relations = [
    Relation(
        ### COMPLETE ###
        
        header =['a', 'b', 'c'],
        tuples =set( (a, b, c) for a in {0, 1, 2}
                        for b in {0, 1, 2}
                        for c in {0, 1, 2}
                        if a > b + c )
        
    ),
    ### COMPLETE ###
    
    Relation(
        header=['c', 'd'],
        tuples =set( (c, d) for c in {0, 1, 2}
                        for d in {0, 1, 2}
                        if c > d )
    )
]


print(len(relations))
print(all(type(r) is Relation for r in relations))