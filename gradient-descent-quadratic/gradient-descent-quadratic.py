def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    # deriviative is 2ax+b = 0
    # maximum /min reaches at dy / dx = 0
    # -b / 2a = x
    ans = x0
    for _  in range(steps):
        grad = 2*a*x0+b
        x0 = x0 - lr * grad 
        ans = x0
    return ans
        