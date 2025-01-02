'''
    Given two string s and t of bits encoding binary numbers Bs and Bt, return a new string of bits
    representing Bs + Bt
'''

def binary_addition(s, t):
    running_sum = 0
    # changing the length of s and t to be additionable :)
    max_len = max(len(s), len(t))
    s = s.zfill(max_len)
    t = t.zfill(max_len)

    result = [0] * max_len
    
    for j in reversed(range(0, max_len)):
        w = int(s[j]) + int(t[j]) + running_sum
        running_sum = 0
        if w > 1:
            running_sum += 1
            w = w % 2
        result[j] = w
    if running_sum != 0:
        result.insert(0, 1)
    return result
        

print(binary_addition("100101", "111101"))
