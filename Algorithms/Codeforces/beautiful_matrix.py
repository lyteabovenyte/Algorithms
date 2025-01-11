l = [[0] * 5] * 5

for i in range(5):
    lst = list(map(int, input().rstrip().split()))
    l[i] = lst


for i in range(5):
    for j in range(5):
        if l[i][j] == 1:
            m, n = i, j
        
print(abs(m - 2) + abs(n - 2))