'''
Constant Complexity    O(1)

example:
    define the duality of the first index in a list

'''

nums = [3, 45, 12, 43, 5345, 2222]

def show(lst):
    if lst[0] % 2 == 0:
        return 'Even'
    return 'Odd'


print(show(nums))