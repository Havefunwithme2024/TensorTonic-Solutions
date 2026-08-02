import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if len(seqs) == 0:
        return np.empty((0, 0), dtype=int)

    if max_len is None:
        max_len = max(map(len, seqs))
    ar = []
    for arr in seqs:
        arr = np.asarray(arr)[:max_len]
        if len(arr) < max_len:
            arr = np.pad(
                arr,
                (0, max_len - len(arr)),
                constant_values=pad_value
            )
        ar.append(arr)

    return np.asarray(ar, dtype=int)