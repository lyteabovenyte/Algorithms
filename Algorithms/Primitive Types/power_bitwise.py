'''
    Write a program that takes a double x and an integer y and retums x^y. 
    You can ignore overflow and underflow.
'''

def bitwise_power(x, y):
    def add(a, b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = (a & k), (b & k)
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = ((carryout << 1, 
                                           k << 1, 
                                           temp_a >> 1, 
                                           temp_b >> 1))
        return running_sum | carryin
    
    def multiply(m, n):
        s = 0
        while m:
            if m & 1:
                s = add(s, n)
            m, n = m >> 1, n << 1
        return s
    
    result = x
    for i in range (y - 1):
        result = multiply(result, x)
    return result

# wanna perform well?
# imagine we have the capabilities of using *
def bitwise_power2(x, y):
    result, power = 1.0, y
    if y < 0:
        x, power = 1/x , -power
    while y:
        if y & 1:
            result *= x
        x, power = x * x, power >> 1  # the latter means (/2)
    return result

print(bitwise_power(0b1101, 2))