'''
    Given a string representing a Roman integer, return if it's valid or not
'''

def valid_or_not(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # a valid roman number is considered to be in non-increasing order.
    # with the exception allowed.
    exceptions = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    i = len(s) - 1
    while i > 0:
        if T[s[i - 1]] < T[s[i]]:
            if s[i - 1] + s[i] in exceptions:
                i -= 2
            else:
                return False
        i -= 1
    return True

print(valid_or_not("LIX"))