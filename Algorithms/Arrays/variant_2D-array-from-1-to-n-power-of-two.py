'''
    Given a dimension d, create a d X d 2D array, which is spiral-order is {1, 2, 3, ..., d^2}
'''
from typing import List

def power_of_two_spiral_order(d):
    # a Trap noticed:
    # to initialize an empty 2D array, don't use
    # d * [[0] * d] --> it's a trap, try it.
    result = [[0] * d for i in range(d)]
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    i = 1
    while i < d ** 2 + 1:
        result[x][y] = i
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(d)
            or next_y not in range(d)
            or result[next_x][next_y] != 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
        i += 1
    return result 


print(power_of_two_spiral_order(3))
