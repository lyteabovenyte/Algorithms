'''
Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
'''
import bisect

# time complexity: O(n)
def partitioning(lst, pivot_index):
    i, j = 0, len(lst) - 1   # first and last element's index
    while i < j:
        if lst[i] > lst[pivot_index]:
            if lst[j] < lst[pivot_index]:
                lst[j], lst[i] = lst[i], lst[j]
                j -= 1
                i += 1
            else:
                j -= 1
        else:
            i += 1
    lst[pivot_index], lst[j] = lst[j], lst[pivot_index]
    return lst
    
# time complexity: O(n)
def better_dutch_flag_partitioning(lst, pivot_index): 
    pivot = lst[pivot_index]
    smaller, equal, larger = 0, 0, len(lst)
    while equal < larger:
        if lst[equal] < pivot:
            lst[smaller], lst[equal] = lst[equal], lst[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif lst[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            lst[larger], lst[equal] = lst[equal], lst[larger]
    return lst


lst = [4, 2, 5, 6, 1, 7, 3, 9]
print(f"partitioning result: {partitioning(lst, 3)}")
print(f"better_dutch_flag_partitioning result: {better_dutch_flag_partitioning(lst, 3)}")

