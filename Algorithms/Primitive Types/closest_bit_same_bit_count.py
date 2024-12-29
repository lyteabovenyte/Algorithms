def closest_bit_same_bit_count(x):
    max_bits = 8   # assume the maximum number of bits of an integer is 8
    for i in range (max_bits -1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 >> i) | (1 >> i + 1)
            return x
    raise ValueError("All bits are 0 or 1.")

print(bin(closest_bit_same_bit_count(0b1110101)))


def weight(x):
    result = 0
    while x:
        x &= x - 1
        result += 1
    return result

print(weight(0b00101010100))
    