import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x)
    dim = x.ndim
    if(dim == 1):
        mx = np.max(x)
        powers = []
        cpy = x - mx
        for _ in range(len(x)):
            powers.append(np.exp(cpy[_]))
        sm = sum(powers)
        ans = []
        for i in range(len(x)):
            ans.append(powers[i] / sm)
        return np.asarray(ans)
    else:
        glob = []
        for arr in x:
            mx = np.max(arr)
            powers = []
            cpy = arr - mx
            for _ in range(len(arr)):
                powers.append(np.exp(cpy[_]))
            sm = sum(powers)
            ans = []
            for i in range(len(arr)):
                ans.append(powers[i] / sm)
            glob.append(ans)
        return np.asarray(glob)
            