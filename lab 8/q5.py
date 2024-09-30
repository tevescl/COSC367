network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.3, # You can change this value
            (False,):0.7
            }
        
    },
    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.4, # You can change this value
            (False,) : 0.6
            }
        
    },    
    
# add more variables

}
            
            
