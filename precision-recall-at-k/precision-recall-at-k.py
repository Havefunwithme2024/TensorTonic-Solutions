def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    lst = recommended[:k]
    a = 0
    for x in relevant:
        if x in lst:
            a+=1
    return [a / k, a / len(relevant)]