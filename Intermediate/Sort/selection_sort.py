def selection_sort(arr):
    size = len(arr)
    i = 0
    while i < size - 1:
        min = i
        j = i + 1
        while j < size :
            if arr[j] < arr[min]:
                min = j
            j += 1
        arr[min], arr[i] = arr[i], arr[min]
        i += 1
    return arr
    
    
    
# another implementation

def find_smallest(arr):
    '''
        return the index of smallest element in an array, to pop and append on new array
    '''
    
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selection_sort2(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr
