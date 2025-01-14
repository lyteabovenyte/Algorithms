'''
    https://codeforces.com/problemset/problem/282/A
'''
from collections import Counter
num_op = int(input())

x = 0
for i in range(num_op):
    op = input()
    c_m = Counter(list(op))
    if c_m["+"] == 2:
        x += 1
    if c_m["-"] == 2:
        x -= 1

print(x)