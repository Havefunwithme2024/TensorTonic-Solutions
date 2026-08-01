import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.asarray(x)
    x = np.where(x == 1, p, 1.0-p)
    phi = (p * (1.0 - p))
    return (x, p, phi)