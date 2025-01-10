'''
    Compute the spiral order of an M X N 2D array.
'''

def spiral_order_of_matrix(m, n):
    result = [(0, 0) for i in range(m * n)]
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    for i in range(m * n):
        result[i] = (x, y)
        x_next, y_next = x + shift[direction][0], y + shift[direction][1]
        if (x_next not in range(m)
            or y_next not in range(n)):
            direction = (direction + 1) & 3
            x_next, y_next = x + shift[direction][0], y + shift[direction][1]
        x, y = x_next, y_next
    return result


print(spiral_order_of_matrix(3, 4))