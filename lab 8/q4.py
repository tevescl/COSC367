from q1 import joint_prob
from q2 import query

"""
network for virus

"""

#Virus is 0.01 chance

# Test A and B for virus
#when virus exist
# Test A 95% recognise virus 
# Test B 90% recognise virus 


#virus dont exits 
#Test A 10% false positive rate (says pos but virus dont exist)
# Test B 5% false positive rate 
network = {
    'Virus' : 
    {
        'Parents': [],
        'CPT' : 
        {
            ():0.01,
        }
    },
    
    'A' : 
    {
        'Parents': ['Virus'],
        'CPT' : 
        {
            (True,):0.95,
            (False,):0.1
        }
    },
    
    'B' : 
    {
        'Parents': ['Virus'],
        'CPT' : 
        {
            (True,):0.9,
            (False,):0.05
        }
    },    
    
    
    }
#answer = query(network, 'Virus', {'A': True})
#print("The probability of carrying the virus\n"
      #"if test A is positive: {:.5f}"
      #.format(answer[True]))