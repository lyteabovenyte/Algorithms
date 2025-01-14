'''
    assuming that keys can take on of the three values, reorder the array so that all objects with the same key appear together
'''

def partition_based_on_key(d):
    l = list(d) # getting the list of the keys
    sorted_l = sorted(l) # sorting the keys
    pivot = sorted_l[len(l) // 2] # getting the pivot -> pivot is the median of the keys, to be in middle.
    smaller, equal, larger = 0, 0, len(l)
    while equal < larger:
        if pivot > l[equal]:
            l[equal], l[smaller] = l[smaller], l[equal]
            smaller, equal = smaller + 1, equal + 1
        elif pivot == l[equal]:
            equal += 1
        else:
            larger -= 1
            l[larger], l[equal] = l[equal], l[larger]

    return(l)


d = {1: 2, 0: 4, 2: 1, 1: 6, 0: 9, 1: 2, 2: 19}
print(partition_based_on_key(d))
