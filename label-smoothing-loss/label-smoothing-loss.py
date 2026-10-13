import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    # Write code here
    
    n = len(predictions)
    q = [0.0]*n
    for i in range(n):
        if i != target:
            q[i] = (epsilon) / n 
            continue
        q[i] = (1.0 - epsilon) + (epsilon)/n 
    entropy = 0.0
    for i in range(n):
        entropy += (q[i]) * math.log(predictions[i])
    return -entropy
        
    
         