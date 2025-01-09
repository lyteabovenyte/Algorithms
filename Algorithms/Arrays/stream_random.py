'''
    Given a Stream of packets, select K elements of the stream randomly in such a way that
    we we always have K elements in the selected packets no less no more.
'''
import itertools
import random

def online_sampling(stream, k):
    # storing the frist k elements
    sampling = list(itertools.islice(stream, k))

    num_seen = k
    for x in stream:
        num_seen += 1
        idx_to_replace = random.randrange(num_seen)
        if idx_to_replace < k:
            sampling[idx_to_replace] = x
    
    return sampling

print(online_sampling([3, 2, 6, 7, 8, 9, 4, 3, 2, 7, 5, 3], 3))