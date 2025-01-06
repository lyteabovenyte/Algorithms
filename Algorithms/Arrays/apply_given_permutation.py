'''
    Given an array A and a permutation P, Apply P to A.
    p = [2, 0, 1, 3] --> move index 0 to index 2, move index 1 to index 0,
    move index 2 to index 1, move index 3 to index 3 (uncahnged).
'''

def apply_permutation(arr, p):
    table = {}
    for i in range(len(arr)):
        table[p[i]] = arr[i]

    for key, value in table.items():
        arr[key] = value

    return arr

def apply2(arr, p):
    res = [0] * len(p)
    for i in range(len(p)):
        res[p[i]] = arr[i]
    return res

print(apply_permutation([3, 6, 5, 4], [1, 0, 3, 2]))
print(apply2([3, 6, 5, 4], [1, 0, 3, 2]))