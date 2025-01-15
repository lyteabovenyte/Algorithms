'''
    Given a valid Roman number, return the corresponding integer
    I: 1
    V: 5
    X: 10
    L: 50
    C: 100
    D: 500
    M: 1000
'''

def roman_to_integer(s):
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    exceptions = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    res, i = 0, 0
    while i < len(s):
        if i + 1 < len(s) and s[i] + s[i + 1] in exceptions:
            res += exceptions[s[i] + s[i + 1]]
            i += 2
        else:
            res += table[s[i]]
            i += 1

    return res

print(roman_to_integer("LIX"))

# the wow approach using functools
import functools

def wow_roman_to_integer(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # going from right to left and if the current_value
    # is less than the one after it, we consider it as 
    # a negative value
    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)), T[s[-1]]
    )

print(wow_roman_to_integer("LIX"))