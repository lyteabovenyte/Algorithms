'''
    a palindromic string is one which reads the same when it is reversed.
'''

# O(n) Time and O(1) Space Complexity.
def is_palindromic(string):
    # NOTE: s[~i] for i in [0, len(s) - 1] is s[-(i + 1)]
    return all(string[i] == string[~i] for i in range(len(string) // 2))


# the final trick :)
def is_palindromic2(string): 
    return string == string[::-1]

print( is_palindromic('garag') )
print( is_palindromic2('garag') )



# NOTE : there is a handy func to check whether a string is palindromic or not

def palinromic(str):
    return str == ''.join([ch for ch in reversed(str)])


print( palinromic('amir') )

