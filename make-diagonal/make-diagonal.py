import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    mat = []
    for i in range(n):
        arr= [0] * n 
        for j in range(n):
            if(i == j):
                arr[i] = v[i]
        mat.append(arr)
    return np.asarray(mat)