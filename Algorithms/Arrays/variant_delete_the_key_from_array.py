'''
    Given an array and a key, delete all the occurence of the key in the array
    and shift the elements, to fill in the emptied spaces.
'''

def delete_key(arr, key):
    i, j = 0, 0
    while i < len(arr):
        if arr[i] == key:
            i += 1
        else:
            arr[j] = arr[i]
            i += 1
            j += 1
    arr[j:] = [0] * (i - j)
    return arr

print(delete_key([2, 3, 5, 5, 7, 5, 11, 13], 5))