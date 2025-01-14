'''
    Given two arrays denoting integers, return their product.
    [2, 3], [1, 2] --> return [2, 8, 6]
'''

def multiply(s, t):
    sign = -1 if (s[0] < 0) ^ (t[0] < 0) else 1
    s[0], t[0] = abs(s[0]), abs(t[0])

    # the multiplication array, has at most len(s) + len(t) elements
    result = [0] * (len(s) + len(t))
    for i in reversed(range(len(s))):
        for j in reversed(range(len(t))):
            result[i + j + 1] += s[i] * t[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # removing the leading zeros
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


print(multiply([-9, 9], [2, 1]))

            