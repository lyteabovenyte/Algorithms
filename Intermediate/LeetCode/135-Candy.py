"""
    https://leetcode.com/problems/candy/
    level: Hard
"""
from typing import List

def candy(ratings: List[int]) -> int:

    N = len(ratings)
    o = [1 for _ in range(N)]

    for i in range(1, N):
        if ratings[i] > ratings[i - 1]:
            o[i] = o[i - 1] + 1, o[i]

    for i in range(N - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            o[i] = max(o[i + 1] + 1, o[i])

    return sum(o)

print(candy([1,6,10,8,7,3,2]))