import numpy as np

def huber_loss(y_true, y_pred, delta):
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    error = y_true - y_pred
    loss = np.where(
        np.abs(error) <= delta,
        0.5 * error**2,
        delta * (np.abs(error) - 0.5 * delta)
    )

    return np.mean(loss)