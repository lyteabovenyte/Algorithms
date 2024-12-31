'''
    reorder a given array IN PLACE, such that the even entries comes first
'''

def mysol(lst):
    i, j = 0, len(lst) - 1  # the first and last index -> j is a placeholder
    while i < j:
        if lst[i] % 2 == 0:
            i += 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1
    return lst


l = [4, 2, 3, 5, 6, 7, 9, 2, 1]
print(mysol(l))
