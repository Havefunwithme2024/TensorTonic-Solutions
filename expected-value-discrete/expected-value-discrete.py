import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    n = len(x)
    f = 0.0
    s = 0.0
    for i in range(n):
        f += x[i] * p[i]
        s+= p[i];
    if s < 1.0 - 1e-6 or s > 1.0 + 1e-6:
        raise ValueError("curry")
    return f
