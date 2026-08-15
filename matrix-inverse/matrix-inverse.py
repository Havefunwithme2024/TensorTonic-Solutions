import numpy as np
from numpy.linalg import det 
from numpy.linalg import inv
def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.asarray(A)
    if A.ndim !=2:
        return None 
    r, c = A.shape
    if r!=c:
        return None
    if det(A) == 0:
        return None
    return inv(A)
