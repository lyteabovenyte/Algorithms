'''
    Given an 2D array, print the maze element.
'''

def maze_traverse(array):
    new_array = []
    outter_index = 0
    while outter_index < len(array):
        inner_array = array[outter_index]
        if outter_index % 2 == 0:
            for i in inner_array:
                new_array.append(i)
        else:
            for i in reversed(inner_array):
                new_array.append(i)
        outter_index += 1
    return new_array


print(maze_traverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))