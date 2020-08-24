import math
import numpy as np

        
# Function responsible for standardizing the data with a mean of 0 and standard deviation of 1
def standardize(dataset):
    n_col = dataset.shape[1]
    
    for col in range(n_col):
        size = len(dataset[:, col])
        mean = sum(dataset[:,col]) / size
        value_i = 0
            
        standard_deviation = np.std(dataset[:,col])
        
        dataset[:,col] = [(value - mean)/standard_deviation for value in dataset[:,col]]
        
    return dataset
    
    
    
    
    


