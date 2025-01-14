'''
    Swapping integer variables, Bitwise
'''

def swap_bitwise(x, y):
    #r = x ^ y --> so x is `r ^ y` and y is `r ^ y`
    x ^= y
    y ^= x
    x ^= y
    return x, y

print(swap_bitwise(6,10))
