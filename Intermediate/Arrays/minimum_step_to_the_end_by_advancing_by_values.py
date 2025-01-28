'''
    Advancing through an array: Given an array of integers that tells you the 
    maximum distance you can advance forward from the given position, 
    compute the minimum number of steps needed to reach the last location.
    (You can advance by any value less than or equal to maximum distance.
'''
from typing import List

# using greedy approach to get the minimum jumps to the end.
def min_step_to_end(arr):
    jump, current_end, farthest = 0, 0, 0
    for i in range(len(arr) - 1):
        farthest = max(farthest, arr[i] + i)
        if i == current_end:
            jump += 1
            current_end = farthest
    return jump

print(min_step_to_end([2, 3, 1, 1, 4]))