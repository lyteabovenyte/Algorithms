'''
    Given an array of integers which each element in the array represents the steps we can advance 
    through the array, i.e in array=[3, 2, 0, 1, 0] and we were starting from index 0, array[0]=3, so
    we can have 0to3 steps forward.
    Write a program which takes an array of n integers, where A[i] denotes the maximum you can
    advance from index i, and returns whether it is possible to advance to the last index starting from
    the beginning of the array.
'''

def advance_through_array(arr):
    furher_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furher_reach_so_far and furher_reach_so_far < last_index:
        furher_reach_so_far = max(furher_reach_so_far, arr[i] + i)
        i += 1
    return furher_reach_so_far >= last_index

print(advance_through_array([2, 3, 0, 0, 1, 0]))
