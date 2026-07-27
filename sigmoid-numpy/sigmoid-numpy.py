import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    # e^x / (1 + e^x);
    # np.exp(x)
    x = np.asarray(x, dtype=float)
    return 1 / (1 + np.exp(-x))