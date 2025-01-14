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

# space complexity: O(n)
def apply2(arr, p):
    res = [0] * len(p)
    for i in range(len(p)):
        res[p[i]] = arr[i]
    return res


# trying to solve it with space complexity of O(1)
def apply_perm(perm, A):
    for i in range(len(A)):
        # check if the element at index i has not been moved
        # by checking if perm[i] is not negative
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # subtracts len(perm) from an entry in perm
            # to make it negative, which indicates the corresponding
            # move has been performed
            perm[next] -= len(perm)
            next = temp
    # Restore temp
    perm[:] = [a + len(perm) for a in perm]
    return A

# the WOW approach
def apply_wow(perm, A):
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    
    return A
