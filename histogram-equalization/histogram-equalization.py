import math
def histogram_equalize(image: list) -> list:
    """
    Returns the histogram-equalized grayscale image.
    """
    # Write code here
    n = len(image)
    m = len(image[0])
    dict = (256) * [0]
    for i in range(n):
        for j in range(m):
            dict[image[i][j]]+=1
    cdf = (256) * [0]
    cdf[0] = dict[0]
    best = math.inf
    if(cdf[0]):
        best = cdf[0]
    total = n*m
    for i in range(1, 256):
        if(i):
            cdf[i] = cdf[i-1] + dict[i]
            if(cdf[i]):
                best = min(best, cdf[i])
    if(n*m == best):
        return [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            image[i][j] = round((cdf[image[i][j]] - best) / (n*m - best) * 255)
    return image
            
    