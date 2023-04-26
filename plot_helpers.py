import numpy as np
import matplotlib.pyplot as plt
from razdel import tokenize
from nltk.probability import FreqDist

def show_tokens_frequency(data_frame, amount):
    tokens = np.array([np.array([w.text for w in list(tokenize(sentence))]) for sentence in data_frame["sentence"]], dtype=object)
    tokens = np.concatenate(tokens)
    dist = FreqDist(tokens)
    toks = [pair[0] for pair in dist.most_common(amount)]
    nums = [pair[1] for pair in dist.most_common(amount)]
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]
    plt.figure(figsize=(20, 10), dpi=100)
    plt.bar(toks, nums)