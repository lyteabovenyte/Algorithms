'''
    https://codeforces.com/problemset/problem/2039/C1
'''
import math

n = int(input())

for _ in range(n):
    lst = list(map(int, input().rstrip().split()))
    x = lst[0]
    m = lst[1]
    res = 0
    for y in range(1, m + 1):
        if x == y:
            continue
        xor = x ^ y
        if xor == 0:
            continue
        if xor > x and xor > y:
            continue
        if x % xor == 0 or y % xor == 0:
            res += 1
    print(res)