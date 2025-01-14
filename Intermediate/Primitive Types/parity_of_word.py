'''
    the parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
    parity checks are used to detect single bit errors in data storage and communications.

'''
# O(n)
# time complexity: O(n)
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
# time complexity: O(n)

def tricky_parity(x):
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
                (same --> 0, diff --> 1) e.g 1001 ^ 1100 = 0101
        '''
        x >>= 1
    
    return result



# time complexity: O(k) --> let the k be the number of Ones in the number
def parity_fiddling(x):

    result = 0 
    while x:
        result ^= 1 # counting trick.
        x &= x - 1  # erasing the last set bit of the number
    return result 



PRECOMPUTED_PARITY = {} # a cache dict with precomputed parirty of 16 bit words

# we consider a 64-bit word, to 4 of 16-bit word.
def parity_with_cache(x): 
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
           PRECOMPUTED_PARITY[x >> (2 * MASK_SIZE) & BIT_MASK] ^
           PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
           PRECOMPUTED_PARITY[x & BIT_MASK])
    

'''
    We illustrate the approach with an 8-bit word. The parity of (11010111) is the same as the parity
    of (1101) XORed with (0111), i.e., of (1010). This in turn is the same as the parity of (10) XORed with
    (10), i.e., of (00). The final result is the XOR of (0) with (0), i.e.,0, Note that the first XOR yields
    (11011010), and only the last 4 bits are relevant going forward. The second XOR yields (11101100),
    and only the last 2 bits are relevant. The third XOR yields (10011010). The last bit is the result, and
    to extract it we have to bitwise-AND with (00000001).
    time complexity: O(logn)
    so the final algorithm for a 64-bit word is similar to:
'''
def parity(x):
    # split the word and check the parity(XOR) of first half with second half
    # up until the last bit represents the parity of the word.
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1  # the last bit is the result, so we extract it with bitwise-AND



    
print( parity_check(0b111011) )
print( tricky_parity(0b111011) )
print( parity_fiddling(0b11011101) ) # 0->True, 1->False

