def seasonal_average(series: list, period: int) -> list:
    """
    Returns the average for each position in the seasonal cycle.
    """
    # Write code here
    n = len(series)
    vis = [False] * n
    ans=[]
    for i in range(n):
        cur=0.0
        le=0
        if(vis[i]):
            continue 
        for j in range(i, n, period):
            cur+=float(series[j])
            vis[j]=True
            le+=1
        cur/=le
        ans.append(cur)
    return ans
        