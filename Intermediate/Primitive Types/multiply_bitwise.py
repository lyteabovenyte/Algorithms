'''
    Write a program that multiplies two nonnegative integers.
    The only operators you are allowed to
    use are:
    1. assignments
    2. thebitwise operators >>, <<, |, &, ~, ^
    3. equality checks and Boolean combinations thereof.
'''

def multiply_bitwise(x, y):
    # helper function for bitwise_adding (without arithmatic operations)
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
    
    running_sum = 0 
    while x:
        if x & 1: 
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum