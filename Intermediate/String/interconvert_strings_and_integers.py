'''
    implement an integer to string conversion function, and a string to integer conversion function.
    
    str_to_int:   input: '123'   output: 123
    int_to_str:   input: 123     output: '123'
    
    you cnanot use library functions like <int> in python.
'''
import functools
import string


def str_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)
    


def int_to_str(x):
    is_negative = False
    if x < 0:
        x ,is_negative = -x, True
        
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
        
    return ('-' if is_negative else '') + ''.join(reversed(s))
        
        


print(int_to_str(-123), type(int_to_str(-123))) # --> -123 <class 'str'>
print( str_to_int('-123'), type(str_to_int('-123') ))
