import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    n = len(fpr)
    s = 0
    for i in range(n-1):
        s += (tpr[i] + tpr[i+1]) * (fpr[i+1]-fpr[i]) / 2.0
    return s
        