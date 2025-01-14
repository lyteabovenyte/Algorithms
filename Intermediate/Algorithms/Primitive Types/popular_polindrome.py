import math

# time complexity: O(n)
def palindrome(x):
    result = 0
    while x:
        prev_result = result
        result = (result * 10) + (x % 10)
        x //= 10
        if x == result or x == prev_result:
            return True
    return False

def better_palindrome(x):
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for i in range(num_digits // 2):
        if x % 10 != x // msd_mask:
            return False
        x %= msd_mask   # removing MSD
        x //= 10        # removing LSD
        msd_mask //= 100
    return True

print(better_palindrome(34543))
print(palindrome(345543))
