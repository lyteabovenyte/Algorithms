'''
    Given a permutation, return the next permutation.
    arr = [1, 0, 3, 2], return --> [1, 2, 0, 3]
'''

def my_sol(perm):
    k = 0
    i = len(perm) - 1
    
    if len(perm) == 1:
        return []

    while i > 0:
        if perm[i] > perm[i - 1]:
            k = i - 1
            break
        if i == 1 :
            return []
        i -= 1

    min_index = 0
    s = float('inf')
    for j in range(k + 1, len(perm)):
        if perm[j] < s and perm[j] > perm[k]:
            s = perm[j]
            min_index = j

    perm[k], perm[min_index] = perm[min_index], perm[k]

    perm[:] = perm[:k + 1] + sorted(perm[k + 1:])
    return perm

def elegant_next_permutation(perm):
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and
           perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
        if inversion_point == -1:
            return []
        
    # since elements after inversion_point are in decreasing order
    # we can iterate from right to left and the first element
    # which is greater than inversion_point's element
    # is what we want to swap
    for i in reversed(range(len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break
    
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm

        
print(my_sol([2, 3, 1]))
print(elegant_next_permutation([2, 3, 1]))

