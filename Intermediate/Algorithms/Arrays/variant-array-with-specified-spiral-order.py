'''
    Given a sequence of integers P, compute an array A whose spiral order is P.
    Assume the size of P is n^2 for some integer n.
'''
import math

def array_with_specified_spiral_order(arr):
    d = int(math.sqrt(len(arr))) # dimension of the result array
    result = [[0] * d for i in range(d)]
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    for ele in arr:
        result[x][y] = ele
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(d)
            or next_y not in range(d)
            or result[next_x][next_y] != 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return result

print(array_with_specified_spiral_order([1, 2, 3, 4, 5, 6, 7, 8, 9]))


