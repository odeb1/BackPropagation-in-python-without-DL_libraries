import numpy as np

def sigmoid(z):
    
    output = 0.0
    #########################################
    # modify this to return z passed through the sigmoid function
    output = 1.0 / (1.0 + np.exp(-z))
    ########################################/
    
    return output

