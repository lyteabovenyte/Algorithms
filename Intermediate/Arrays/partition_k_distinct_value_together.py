'''
    Given an array of k distinct values, reorder them in such a way that specific values come together in the array
'''
from collections import Counter

def partition_k_distinct_values_together(l):
    c_m = Counter(l)

    # in place approach.
    j = 0
    for key, value in c_m.items():
        l[j: j + value] = [key] * value
        j += value

    return l

print(partition_k_distinct_values_together([0, 1, 2, 1, 2, 3, 1, 2, 1, 0]))
