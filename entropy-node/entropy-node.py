import numpy as np
from math import log2
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    freq = {}
    for label in y:
        freq[label] = freq.get(label, 0) + 1
    total = sum(freq.values())
    ans = 0.0
    for _, count in freq.items():
        p = count / total
        ans -= p * log2(p)
    return ans
        