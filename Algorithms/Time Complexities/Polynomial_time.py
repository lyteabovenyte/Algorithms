'''
Polynomial time    O(n^n) --> which the second n is the number of survey in the list

example:
    Bubble sort --> O(n^2)

'''

nums = [34, 25, 12, 22, 11, 64, 90]


def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            break
    return lst 


print(bubble_sort(nums))