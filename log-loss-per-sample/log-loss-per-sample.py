import math
from numpy import clip
def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    ans = []
    for i in range(len(y_true)):
        cl = clip(y_pred[i], eps, 1-eps)
        v = -(y_true[i] * math.log(cl) + (1 - y_true[i]) * math.log(1 - cl))
        ans.append(v)
    return ans