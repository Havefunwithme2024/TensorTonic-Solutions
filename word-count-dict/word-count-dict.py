def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    dict={}
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if(sentences[i][j] in dict):
                dict[sentences[i][j]]+=1
            else:
                dict[sentences[i][j]]=1
    return dict