'''
    Given a decimal string which denotes ip addresses and an integer k which denotes the number
    of periods in ip addresses, imagine the string's length in unbounded,
    return all the possible valid IP addresses with k periods in between.
'''
# We would handle this recursively, first selecting where to place the first period, 
# then recursing on k-1 periods and the string that starts after the period we just inserted.  
# We would not actually copy the substring to pass recursively,
# but just use a start index to prevent excess space complexity.

# TODO!!