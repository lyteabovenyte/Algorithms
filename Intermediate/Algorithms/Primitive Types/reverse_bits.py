import math

# time complexity: O(n^2)
def reverse_bits(x):
    d = {}
    n = x.bit_length()
    for i in range (n):
        d[i] = (x >> i) & 1
    
    result = 0
    for j in range(n):
        if d[j] == 1:
            result += (2 ** (n - 1 - j))
    
    return bin(result)

# time complexity: O(n/2)
def reverse_bit2(x):
    n = x.bit_length()
    for i in range(math.floor(n/2)): 
        lsb = n - i - 1
        msb = i
        if ((x >> lsb) & 1 != (x >> msb) & 1):
            # then perform swap bits using bitmask
            bitmask = (1 << lsb) | (1 << msb)
            x ^= bitmask
    return x
    
# with the usage of cache and lookup table.
PRECOMPUTED_REVERSE = {
    0b00: 0b00,
    0b01: 0b10,
    0b10: 0b01,
    0b11: 0b11,
}

# x is 8 bit integer and we chunk it to 2 bit.
# time complexity: O(n/l) for n:integer size and l:cache size
def reverse_bit_with_cache(x):
    mask_size = 2
    bit_mask = 0b11
    return (
        PRECOMPUTED_REVERSE[x & bit_mask] << 3 * mask_size |
        PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << 2 * mask_size |
        PRECOMPUTED_REVERSE[(x >> 2 * mask_size) & bit_mask] << mask_size |
        PRECOMPUTED_REVERSE[(x >> 3 * mask_size) & bit_mask]
    )

print(bin(reverse_bit_with_cache(0b10100111)))
