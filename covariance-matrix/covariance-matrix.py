import numpy as np

def covariance_matrix(X):
    X = np.asarray(X, dtype=float)

    mean = np.mean(X, axis=0)
    X = X - mean
    if X.ndim != 2:
        return None
    rows, cols = X.shape
    if rows < 2:
        return None
    return (X.T @ X) / (rows - 1)