def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """
    # Write code here
    a = []
    a.append(series[0])
    b=[]
    b.append(series[1]-series[0])
    for i in range(1,len(series)):
        a.append(alpha*series[i]+(1.0-alpha)*(a[i-1]+b[i-1]))
        b.append(beta*(a[i]-a[i-1]) + (1.0-beta)*b[i-1])
    return a