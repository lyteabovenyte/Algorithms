'''
    hell no!
    https://codeforces.com/problemset/problem/281/A
'''
input = str(input())

l = list(input)
if ord(l[0]) > 96:
    l[0] = chr(ord(l[0]) - 32)

print("".join(l))