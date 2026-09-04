def user_based_cf_prediction(similarities: list, ratings: list) -> float:
    """
    Returns the positive-similarity weighted rating prediction.
    """
    # Write code here
    similarity_sum = 0.0
    N = len(similarities)
    rating_sum = 0.0
    for i in range(N):
        rating_sum+=max(0.0, ratings[i]*similarities[i])
        similarity_sum+=max(0.0, similarities[i]);
    if(similarity_sum == 0.0):
        return 0.0
    return rating_sum / similarity_sum
    