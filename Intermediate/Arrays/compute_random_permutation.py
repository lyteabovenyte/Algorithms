'''
    Given an integer n, compute a random permutation of elements {0, 1, 2, 3, ..., n -1}
'''
import random

def random_permutation(n):
    permutation = list(range(n))
    # same as offline sampling permutation. 
    for i in range(n):
        r = random.randint(i, n - 1)
        permutation[i], permutation[r] = permutation[r], permutation[i]
    return permutation


print(random_permutation(5))