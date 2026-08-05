import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    x = x  / (1.0 + np.exp(-x));
    return x
    