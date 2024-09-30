import itertools, copy 
from csp import scope, satisfies, CSP


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in scope(c)}
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = []
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.append(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(c):
                    for z in scope(cprime):
                        if x != z:
                            tda.add((z, cprime))
    return csp

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: y for x, y in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment
            

domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda o, r, c1    :   o + o == r + 10 * c1, # one of the constraints
        # add more constraints
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == 6,
        
        lambda o, w, u, c1, c2: ((o + o) // 10 + w + w) % 10 == u and (o + o) // 10 == c1,

        lambda w, t, o, c1, c2: ((w + w) // 10 + t + t) % 10 == o and (w + w) // 10 + (t + t) // 10 == c1 + c2,

        lambda t: t + t >= 10,

        lambda f: f == 1,        
     
        
        })


new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])