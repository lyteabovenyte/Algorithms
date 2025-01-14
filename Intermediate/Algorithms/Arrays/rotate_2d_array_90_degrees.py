'''
    Given an 2D array, rotate it by 90 degrees.
'''

def rotate_90(arr):
    return [list(reversed(ele)) for ele in list(zip(*arr))]


print(rotate_90([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))