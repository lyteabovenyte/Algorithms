'''
    https://codeforces.com/contest/1632/problem/B
'''

tt = int(input())

while tt > 0:

    n = int(input())
    p = 1
    while (p * 2 < n):
        p <<= 1  # p *= 2
    for i in reversed(range(p)):
        print(i, end=" ")
    print(p, end=" ")
    for i in range(p + 1, n):
        print(i, end=" ")
    
    print()
    tt -= 1