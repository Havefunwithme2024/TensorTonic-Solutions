from math import cos
from math import pi
def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    # Write code here
    lr = min_lr + 1.0/2.0 * (base_lr - min_lr)* (1.0 + cos(pi * current_step / total_steps))
    return lr