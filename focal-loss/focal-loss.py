import numpy as np

def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    p=np.asarray(p,dtype=float)
    y=np.asarray(y)
    return float(np.mean(-((1.0-p)**gamma)*y*np.log(p) - (p**gamma) *(1.0-y)*np.log(1.0-p)))
    