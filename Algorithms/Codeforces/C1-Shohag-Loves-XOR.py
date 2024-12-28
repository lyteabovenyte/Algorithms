n = int(input())

for i in range(n - 1):
    x = int(input()[0])
    m = int(input()[2])
    res = 0
    for y in range(m):
        xor = x ^ y
        if xor == 0:
            continue
        if x % xor == 0 or y % xor == 0:
            res += 1
    print(res)