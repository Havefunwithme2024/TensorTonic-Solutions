import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    freq = Counter(x)
    mean = sum(x) / len(x)
    x.sort()
    median = 0
    if len(x) % 2:
        median = x[len(x) // 2]
    else:
        median = (x[len(x) // 2] + x[(len(x) // 2) -1]) / 2
    mode = 1e9
    frq = 0
    for val, f in freq.items():
        if(f > frq or (frq == f and mode > val)):
            frq = f 
            mode = val
    return (mean, median, mode)