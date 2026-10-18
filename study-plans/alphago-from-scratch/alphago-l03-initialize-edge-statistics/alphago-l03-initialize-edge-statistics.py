import numpy as np

def initialize_mcts_edges(policy_logits: np.ndarray, legal_mask: np.ndarray) -> dict:
    """
    Returns: N as an int64 array; W, Q, and P as float64 arrays in a dictionary.
    """
    policy_logits=np.asarray(policy_logits, dtype=np.float64)
    legal = policy_logits[legal_mask] - policy_logits[legal_mask].max()
    weights = np.exp(legal)
    priors=np.zeros(policy_logits.size, dtype=np.float64)
    priors[legal_mask] = weights/weights.sum()
    return {
        "N": np.zeros(policy_logits.size, dtype=np.int64),
        "W": np.zeros(policy_logits.size, dtype=np.float64),
        "Q": np.zeros(policy_logits.size, dtype=np.float64),
        "P": priors,
    }