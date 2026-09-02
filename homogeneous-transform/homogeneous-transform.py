import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    points = np.asarray(points)
    dim = points.ndim
    if(dim == 1):
        #(4, 4) * (1, 4)
        points = np.append(points, 1)
        points = np.transpose(points)
        points = T @ points 
        k = len(points)
        return points[:k-1]
    points = np.c_[points, np.ones(points.shape[0])]
    return (points @ np.asarray(T).T)[:, :3]
        