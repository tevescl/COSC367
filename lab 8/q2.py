from q1 import joint_prob

from itertools import product
""""

return a pair of numbers (probFalse, probTrue) 
in which this is from the distribution of the network
"""

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    
    # Initialise a raw distribution to [0, 0]
    answer = [0.0,0.0]
    assignment = dict(evidence) # create a partial assignment
    
    # 2 for loops first for query then hidden 
    
    for query_value in {True, False}: 
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        
        for values in product((True, False), repeat=len(hidden_vars)): 
            # Update the assignment (we now have a complete assignment)
              
            hidden_assignments = {var: val for var, val in zip(hidden_vars, values)}
            
            
            assignment.update(hidden_assignments)
            
            # Update the raw distribution by the probability of the assignment.
            prob = joint_prob(network, assignment)
            
            
            answer[query_value] += prob    
            
    # Normalise the raw distribution and return it
   
    answer = [x / (sum(answer)) for x in answer] if (sum(answer)) > 0 else answer
    return (answer[False],answer[True])
            
#network = {
    #'Burglary': {
        #'Parents': [],
        #'CPT': {
            #(): 0.001
            #}},

    #'Earthquake': {
        #'Parents': [],
        #'CPT': {
            #(): 0.002,
            #}},
    #'Alarm': {
        #'Parents': ['Burglary','Earthquake'],
        #'CPT': {
            #(True,True): 0.95,
            #(True,False): 0.94,
            #(False,True): 0.29,
            #(False,False): 0.001,
            #}},

    #'John': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.9,
            #(False,): 0.05,
            #}},

    #'Mary': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.7,
            #(False,): 0.01,
            #}},
    #}

#answer = query(network, 'John', {'Mary': True})
#print("Probability of John calling if\n"
      #"Mary has called: {:.5f}".format(answer[True]))