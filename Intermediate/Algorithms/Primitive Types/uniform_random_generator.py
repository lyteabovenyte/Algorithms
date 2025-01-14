'''
    This problem is motivated by the following scenario. Six friends have to select a designated driver
    using a single unbiased coin. The process should be fair to everyone.
    How would you implement a random number generator that generates a random integer I between a
    and b, inclusive, given a random number generator that produces zero or one with equal probability?
    All values [a,b] should be equally likely.
'''
import random

# mock a random generator which return 0 or 1
def zero_one_generator():
    lst = [0, 1]
    return random.choice(lst)

def uniform_random_generator(lower_bound, upper_bound):
    number_of_outcome = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcome:
            result = (result << 1) | zero_one_generator()
            i += 1
        if result < number_of_outcome:
            break
    return result + lower_bound


print(uniform_random_generator(0, 4))
