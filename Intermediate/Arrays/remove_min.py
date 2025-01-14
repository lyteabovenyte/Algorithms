'''
remove the minumim element of an array
'''

def remove_min(arr):
    if len(arr) == 0:
        return arr
    
    min_value = arr[0]
    
    for i in range(len(arr)):
        if arr[i] <= min_value:
            min_value = arr[i]
            wanted_indice = i
            
    removed_element = arr.pop(wanted_indice)
    return f'{arr} and the poped element is {removed_element}'
    
    


print(remove_min([2, 5, 3, 6, 3, -1])) # --> [2, 5, 3, 6, 3] and the poped element is -1