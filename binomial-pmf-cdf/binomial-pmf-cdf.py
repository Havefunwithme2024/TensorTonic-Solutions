import numpy as np
from scipy.special import comb
from scipy.special import gammaln

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    log_pmf = (
    gammaln(n + 1)
    - gammaln(k + 1)
    - gammaln(n - k + 1)
    + k * np.log(p)
    + (n - k) * np.log(1 - p)
)
    pmf = np.exp(log_pmf)
    cdf = 0.0
    for i in range(k + 1):
        log_term = (
            gammaln(n + 1)
            - gammaln(i + 1)
            - gammaln(n - i + 1)
            + i * np.log(p)
            + (n - i) * np.log(1 - p)
        )
        cdf += np.exp(log_term)
    return pmf, cdf