# time complexity: O(1)
def swap_bits(x, i, j):
    # check whether the values at the index ith, jth
    # of the x differs
    if (x >> i) & 1 != (x >> j) & 1:
        # creating the bitmask needed to flip the values
        # at the indices, the using XOR to perform the flip
        bitmask = (1 << i) | (1 << j)
        x ^= bitmask
    return x