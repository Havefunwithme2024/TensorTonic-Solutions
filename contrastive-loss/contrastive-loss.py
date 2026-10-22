import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean"):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    y = np.asarray(y, dtype=float)
    differences = a - b
    if differences.ndim == 1:
        differences = differences[None, :]
    distances = np.linalg.norm(differences, axis=1)
    positive_loss = y * distances ** 2
    negative_loss = (1.0 - y) * np.maximum(0.0, margin - distances) ** 2
    losses = positive_loss + negative_loss
    if reduction == "mean":
        return float(np.mean(losses))
    return float(np.sum(losses))
    