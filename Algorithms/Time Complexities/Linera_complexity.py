'''
Linear complexity    O(n)

example:
    finding the index of an element in a non sorted list

'''

nums = [76, 34, 93, 25, 14, 99, 38]

def show(lst, element):
    for i in lst:
        if i == element:
            return lst.index(i)
        
        
print(show(nums, 25))