t = int(input())

while t > 0:
    length = int(input())
    num = input()
    result = "YES" if length == 1 or (length == 2 and num[0] != num[1]) else "NO"
    print(result)
    t -= 1
