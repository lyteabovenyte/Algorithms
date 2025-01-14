'''
    Given an n X n 2D array, return the elements in the spiral ordering.
'''
from typing import List

def spiral_ordering_of_matrix(matrix: List[List[int]]) -> List[int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(matrix) - offset - 1:
            # matrix has odd dimentsion, and we are in the center
            # of the matrix
            spiral_ordering.append(matrix[offset][offset])
            return
        
        spiral_ordering.extend(matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(
            list(zip(*matrix))[-1 - offset][offset:-1 - offset]
        )
        spiral_ordering.extend(
            matrix[-1 - offset][-1 - offset:offset: -1]
        )
        spiral_ordering.extend(
            list(*zip(matrix))[offset][-1 - offset:offset: -1]
        )

    spiral_ordering: List[int] = []
    for offset in range((len(matrix) + 2) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering


# the "processing array in shell" approach
def matrix_processing_in_shell(matrix: List[List[int]]) -> List[int]:
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0)) # controls the direction at the end of the shell.
    direction = x = y = 0
    spiral_ordering: List[int] = []
    for _ in range(len(matrix) ** 2):
        spiral_ordering.append(matrix[x][y])
        matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(matrix))
            or next_y not in range(len(matrix))
            or matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_y, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering

