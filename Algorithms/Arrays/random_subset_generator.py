'''
    Given an integer n and an integer k, generate a subset of {1, 2, ..., n - 1} with size k.
'''
import random

def random_subset(n, k):
    changed_elements = {}
    for i in range(k):
        r = random.randrange(i, n)
        change_element_mapped = changed_elements.get(r, r)
        i_mapped = changed_elements.get(i, i)
        changed_elements[r] = i_mapped
        changed_elements[i_mapped] = change_element_mapped
    return [changed_elements[i] for i in range(k)]

print(random_subset(100, 4))