import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    N = len(y)
    K = 0
    if(num_classes == None):
        K = max(y)+1
    else:
        K =num_classes
    arr = []
    for i in range(N):
        temp = [0] * K
        for j in range(K):
            if j == y[i]:
                temp[j] = 1
        arr.append(temp)
    return np.asarray(arr)