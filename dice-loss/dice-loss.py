import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    p = np.asarray(p, dtype=float)
    y = np.asarray(y,dtype=float)
    return float(1.0 - (2.0 * np.sum(p*y) + eps) / (np.sum(p) + np.sum(y) + eps))