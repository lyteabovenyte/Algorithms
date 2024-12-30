'''
    Given two positive integers, compute their quotient, using only the addition, subtraction, and
    shifting operators.
'''
# time complexity: O(n)

def divide_bitwise(x, y):
    result, power = 0, 32      # imagine the number is 64-bit length
    y_power = y << power       # (2^k)y
    while x >= y: 
        while y_power > x:
            # finding the right k which (2^k)y is less than x
            y_power >>= 1
            power -= 1
        
        result += 1 << power   # adding 2^k to the result
        x -= y_power
    return result
