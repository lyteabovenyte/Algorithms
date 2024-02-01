'''
    the parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
    parity checks are used to detect single bit errors in data storage and communications.

'''

def parity_check(x):
    num_one_bits = 0
    
    while x:
        num_one_bits += x & 1
        x >>= 1
        
    if num_one_bits % 2 == 0:
        return 0
    else:
        return 1
    
    
# a tricky solution

def parity(x):
    '''
        since we only care if the number of 1s is even or odd, we can store the number mod 2
    '''    
    result = 0
    
    while x:
        result ^= x & 1
        '''
                x ^ y:
                Does a "bitwise exclusive or".
                Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
                and it's the complement of the bit in x if that bit in y is 1.
        '''
        x >>= 1
    
    return result
    
    
print( parity_check(0b111011) )
print( parity(0b111011) )

