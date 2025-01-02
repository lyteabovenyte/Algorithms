'''
    Given an array of boolean-valued, reorder them in such a way that False goes first and True goes last, also
    keep the relative ordering of True values.
'''

# to keep the relative ordering of True values, we should iterate from the right
def partition_boolean_valued_relative(l):
    i, j = 0, len(l) - 1
    while j > i:
        if l[j] == True:
            j -= 1
        else:
            l[j], l[i] = l[i], l[j]
            i += 1
    return l


print(partition_boolean_valued_relative([True, False, True, False, False, True, True]))