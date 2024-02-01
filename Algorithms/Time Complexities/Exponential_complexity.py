'''
Exponential complexity    O(n^n) --> the first n is often a number


example:
    the combination of elements in a list

'''

from itertools import chain, combinations


def subset(iterable):
    lst = list(iterable)
    return chain.from_iterable(combinations(lst, r) for r in range(len(lst) + 1))


print(list(subset(['a', 'b', 'c'])))