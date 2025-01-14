'''
    InteConverting str to int and int to str without buildin functions: `int` and `str`
'''

def str_to_int(s):
    integers = [ord(i) - 48 for i in list(s)]
    sign = -1 if integers[0] < 0 else 1
    if sign == -1:
        del integers[0]
    p, res = 0, 0
    for ele in reversed(integers):
        if p == 0:
            res += ele
        else:
            res += ele * (10 ** p)
        p += 1
    return sign * res

print(str_to_int("-0234"))

def int_to_str(integer):
    sign = 1
    if integer < 0:
        sign = -1
        integer *= -1
    l = [chr(i + 48) for i in list(map(int, str(integer)))]
    if sign == -1:
        return sign + "".join(l)
    return "".join(l)


def int_to_str2(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))

print(int_to_str2(-12345))

import functools, string

def str_to_int2(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0
    ) * (-1 if s[0] == '-' else 1)

print(str_to_int2("-01203"))
