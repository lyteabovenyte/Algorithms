'''
    given an array of four distinct keys, we want to partition them, so that the keys with the same value stick together.
'''

# the approach is kinda similar
def partition_by_key(l):
    # l has 4 distinct values, so we can choose 2 pivots and sort by them
    # but it takes O(n^2) but we will try
    sorted_l = sorted(l)
    pivot1 = sorted_l[len(l) // 2]
    pivot2 = sorted_l[len(l) // 2 + 1]
    pivots = [pivot1, pivot2]
    for i in range(2):
        pivot = pivots[i]
        smaller, equal, larger = 0, 0, len(l)
        while equal < larger:
            if pivot > l[equal]:
                l[equal], l[smaller] = l[smaller], l[equal]
                equal, smaller = equal + 1, smaller + 1
            elif pivot == l[equal]:
                equal += 1
            else:
                larger -= 1
                l[larger], l[equal] = l[equal], l[larger]
    return l

print(partition_by_key([1, 0, 3, 2, 0, 1, 3, 2, 1]))

