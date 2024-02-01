'''
    Sometimes you need to limit array result to use. Such as you only need the 
    value over 10 or, you need value under than 100. By use this algorithms, you
    can limit your array to specific value

    If array, Min, Max value was given, it returns array that contains values of 
    given array which was larger than Min, and lower than Max. You need to give
    'unlimit' to use only Min or Max.

    ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

    Complexity = O(n)
'''

# First solution
def limit(arr, min=None, max=None):
    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)
    
    return [val for val in arr if min_check(val) and max_check(val)]


# Second solution 
def limit(arr, min=None, max=None):
    if len(arr) == 0:
        return arr
    
    if min is None:
        min = min(arr)
        
    if max is None:
        max = max(arr)
        
    return list(filter(lambda val: min <= val <= max, arr))


