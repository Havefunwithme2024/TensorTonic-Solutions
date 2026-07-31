import numpy as np
from numpy.linalg import norm

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    denom = norm(a) * norm(b)
    if denom == 0:
        return 0.0
    return np.dot(a, b) / (denom)