'''
    Given an array of distinct element and a size, implement an algorithm that returns
    a subset of the given size of the array element. All subsets should be equally likely.
    Return the result in input array itself.
'''
import random

def sample_offline_data(stream, k):
    for i in range(k): 
        # generate a random index in [i, len(stream) - 1]
        r = random.randint(i, len(stream) - 1)
        stream[r], stream[i] = stream[i], stream[r]
    
    return stream


print(sample_offline_data([3, 7, 5, 11], 3))