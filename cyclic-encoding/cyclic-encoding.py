import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    # Write code here
    lst = []
    for i in range(len(values)):
        val = (values[i] * 2.0 * math.pi) / period 
        lst.append([math.sin(val), math.cos(val)])
    return lst