"""
    https://leetcode.com/problems/zigzag-conversion
    level: Medium
"""

def zigzag_conversion(s: str, num_rows: int) -> str:
    N = len(s)
    res = [[]  for _ in range(num_rows)]

    if num_rows == 1:
        return s

    direction = 1
    j = 0
    for i in range(N):
        res[j].append(s[i])
        next_j = j + direction

        if next_j > num_rows - 1:
            direction = -1
            next_j += direction * 2
        if next_j < 0:
            direction = 1
            next_j += direction * 2
        j = next_j

    return "".join([item for ele in res for item in ele])


print(zigzag_conversion("PAYPALISHIRING", 3))