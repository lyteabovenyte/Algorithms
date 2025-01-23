'''
    https://codeforces.com/problemset/problem/158/A
'''

inp = list(map(int, input().rstrip().split())) # n, k
k = inp[1]
scores = list(map(int, input().rstrip().split())) # scores

kth_grade = scores[k - 1]

out = 0
for ele in scores:
    if ele > 0 and ele >= kth_grade:
        out += 1
    else:
        break

print(out)
        



