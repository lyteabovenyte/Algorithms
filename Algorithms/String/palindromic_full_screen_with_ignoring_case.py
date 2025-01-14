'''
    Given a string, remove all nonalphabetical characters, see if the whole string is palindromic or not.
'''
import string

def palindromic_whole_string(s):
    l = [ele.lower() for ele in s if ele in string.ascii_letters]

    i, j = 0, len(l) - 1
    while i <= j:
        if l[i] != l[j]:
            return False
        i, j = i + 1, j - 1
    
    return True

# alphanumeric version
def alphanumeric_palindromic(s):
    i, j = 0, len(s) - 1
    while i <= j:
        while not s[i].isalnum() and i <= j:
            i += 1
        while not s[j].isalnum() and i <= j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True
    

print(palindromic_whole_string("Able was I, ere I=1 saw Elba!"))
print(alphanumeric_palindromic("Able was I, ere I=1 saw Elba!!"))





