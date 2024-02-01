'''
    problem at : https://codeforces.com/problemset/problem/236/A
'''

username = input()

d = {}

for c in username:
    d[c] = d.get(c, 0) + 1
    
if len(d.keys()) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')