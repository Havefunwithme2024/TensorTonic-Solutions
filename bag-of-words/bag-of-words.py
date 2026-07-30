import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    freq = {}
    for word in tokens:
        if word in freq: 
            freq[word]+=1
        else:
            freq[word] = 1
    ans = []
    for i in range(len(vocab)):
        a = 0
        if vocab[i] in freq:
            a = freq[vocab[i]]
        ans.append(a)
    return np.asarray(ans, dtype=int)
        