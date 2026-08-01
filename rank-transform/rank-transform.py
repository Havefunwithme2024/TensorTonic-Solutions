def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    copy = sorted(values)
    freq = {}
    for index in range(len(values)):
        if copy[index] not in freq:
            freq[copy[index]] = []
        freq[copy[index]].append(index+1)
    ans = []
    for val in values:
        s = sum(freq[val]) / len(freq[val])
        ans.append(s)
    return ans