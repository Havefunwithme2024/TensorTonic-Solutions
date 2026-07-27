import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    
    n= len(A)
    m = len(A[0])
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        arr = []
        for j in range(n - 1, -1, -1):
            arr.append(A[j][i])
        matrix[i] = arr[::-1]
        
    return np.asarray(matrix)
            
