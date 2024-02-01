'''
    wirte a program which takes as input two strings s and t of bits encoding binary numbers Bs and Bt,
    respectively, and returns a new string of bits representing the number Bs + Bt.
'''

def binary_sum(s, t):
    arr1 = [int(ch) for ch in s]
    arr2 = [int(ch) for ch in t]
    
    differ_of_length = abs(len(arr1) - len(arr2))
    
    for _ in range(differ_of_length):
        if len(arr1) < len(arr2):
            arr1.insert(0, 0)
        else:
            arr2.insert(0, 0)
            
    #making sure that we have space on the left side of the integers to add the carry-out number
    arr1.insert(0, 0)
    arr2.insert(0, 0)
            
            
    for i in reversed(range(0, len(arr1))):
        t = arr1[i] + arr2[i]
        if t < 2:
            arr1[i] = t
        elif t == 2:
            arr1[i] = 0
            arr1[i - 1] += 1
        elif t > 2:
            arr1[i] = 1
            arr1[i - 1] += 1
            
    return arr1
    
    
    
    
print( binary_sum('100111', '101011') )


