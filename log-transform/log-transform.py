from math import log

def log_transform(values):
    values = [log(value + 1) for value in values]
    return values