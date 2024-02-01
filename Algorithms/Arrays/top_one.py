"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a 
representative value in an array.

This algorithm gets an array, makes a dictionary of it,
 finds the most frequent count, and makes the result list.

For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]

(TL:DR) Get mathematical Mode
Complexity: O(n)
"""

def top_one(arr):
    values = {}
    result = []
    
    for i in arr:
        values[i] = values.get(i, 0) + 1
        
    max_value = max(values.values())
    
    for key, value in values.items():
        if value == max_value:
            result.append(key)
            
    return f'{result} with the repition of {max_value}'
        


print(top_one([1, 1, 1, 2, 2, 3, 4])) # --> [1] with the repition of 3