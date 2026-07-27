import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.asarray(x)# Write code here
    return np.maximum(0, x);