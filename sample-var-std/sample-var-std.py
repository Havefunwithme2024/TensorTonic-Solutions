import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.mean(x)
    x = (x-mean)**2
    val = np.sum(x)
    s =val / (len(x)-1)
    stdev = np.sqrt(s)
    return (s, stdev)