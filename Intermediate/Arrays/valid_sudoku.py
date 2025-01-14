'''
    Given a 9 X 9 2D array (Sudoku) which is partially compeleted (blank sqaures are 0)
    return if it's valid or not.
'''
import collections
import math

def is_valid_sudoku(partial_assignment):
    def has_duplicates(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
    
    n = len(partial_assignment)
    if any(
        has_duplicates([partial_assignment[i][j] for j in range(n)])
        or has_duplicates([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
        ):
        return False
    
    # check region constraint
    region_size = int(math.sqrt(n))
    return all(not has_duplicates(
        [
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
        ])
        for I in range(region_size) for J in range(region_size)
    )


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(collections.Counter(
        k for i, row in enumerate(partial_assignment)
        for j, c in enumerate(row) if c != 0
        for k in ((i, str(c)), (str(c), j),
                  (i // region_size, j // region_size, str(c)))).values(),
               default=0) <= 1
