def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will eventually hold the value we are interested in
    for var in network:
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 
        curr_cpt = network[var].get('CPT')
        #print ((curr_cpt))
        curr_parent = network[var].get('Parents')
        #print (curr_parent)
        # CPT value is a dictionary
        #this dictionary contains the bools assigned to the parents
        key = () if not curr_parent else tuple(assignment[parent]for parent in curr_parent)
        
        # Update p by multiplying it by probablity var=true or var=false
        p*= curr_cpt[key] if assignment[var] else 1 -curr_cpt[key]
        
        # depending on how var appears in the given assignment.
    
    return p 
########TEST 1

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.2
            #}},
#}

#p = joint_prob(network, {'A': True})
#print("{:.5f}".format(p))


########TEST 2 
#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.1
            #}},
            
    #'B': {
        #'Parents': ['A'],
        #'CPT': {
            #(True,): 0.8,
            #(False,): 0.7,
            #}},
    #}
 
#p = joint_prob(network, {'A': False, 'B':True})
#print("{:.5f}".format(p)) 