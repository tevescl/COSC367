from q1 import joint_prob
from q2 import query

"""
belief network e.g. for Diseaes 

"""

# prob of Disease 1 in 100,000 people
# probPos if person has Disease is 99%
# 

network = {
    'Disease' : {
        'Parents' : [],
        'CPT':{
            (): 0.00001
            }
        
    },
    
    'Test': {
        'Parents': ['Disease'],
        'CPT' : {
            (True,): 0.99,
            (False,): 0.01,
            }
        
        }
    }
#answer = query(network, 'Disease', {'Test': True})
#print("The probability of having the disease\n"
      #"if the test comes back positive: {:.8f}"
      #.format(answer[True]))
      
#answer = query(network, 'Disease', {'Test': False})
#print("The probability of having the disease\n"
      #"if the test comes back negative: {:.8f}"
      #.format(answer[True]))
