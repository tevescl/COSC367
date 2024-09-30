from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: y for x, y in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment


#Q2
#crossword_puzzle = CSP(
    #var_domains={
        ## read across:
        #'across1': set(word for word in "bus has".split() if len(word) == 3),
        #'across3': set(word for word in "lane year".split() if len(word) == 4),
        #'across4': set(word for word in "ant car".split() if len(word) == 3),
        ## read down:
        #'down1': set(word for word in "buys hold".split() if len(word) == 4),
        #'down2': set(word for word in "search syntax".split() if len(word) == 6),
    #},
    #constraints={
        #lambda across1: len(across1) == 3,  
        #lambda across3: len(across3) == 4,  
        #lambda across4: len(across4) == 3,  
        #lambda down1: len(down1) == 4,      
        #lambda down2: len(down2) == 6,        
        #lambda across1, down1: across1[0] == down1[0],
        #lambda down1, across3: down1[2] == across3[0],
        #lambda across1, down2: across1[2] == down2[0],
        #lambda down2, across3: down2[2] == across3[2],
        #lambda down2, across4: down2[4] == across4[0],
    #})

## Print sorted domain for 'across1'
#print(sorted(crossword_puzzle.var_domains['across1']))

# Q3 - EXACTLY THE SAME AS CODE PROVIDED IN QUIZSERVER 
from csp import CSP
canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })