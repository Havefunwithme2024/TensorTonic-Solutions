def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    n = len(returns)
    wealth=1.0
    ans=[]
    for i in range(n):
        wealth=wealth*(1.0+returns[i])
        ans.append(wealth-1.0)
    return ans
    