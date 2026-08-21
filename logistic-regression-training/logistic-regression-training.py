import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1 / (1 + np.exp(-z)), np.exp(z) / (1 + np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (weights, bias).
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    N, D = X.shape
    weights = np.zeros(D)
    bias = 0.0
    for _ in range(steps):
        linear_model = X @ weights + bias
        p = _sigmoid(linear_model)
        dw = (1 / N) * (X.T @ (p - y))
        db = (1 / N) * np.sum(p - y)
        weights -= lr * dw
        bias -= lr * db
        
    return (weights, bias)