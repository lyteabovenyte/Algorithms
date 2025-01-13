'''
    convert spreadsheet column encoding
    A -> 1, B -> 2, ..., AA -> 27, AB -> 28, ..., ZZ -> 702
'''

# the hashmap to map each letter to the corresponding number
# ord(letter) - 64

import functools

def spreadsheet_col_encoding(s: str):
    return functools.reduce(
        lambda x, c: x * 26 + (ord(c) - 64), 
        s, 0
    )

print(spreadsheet_col_encoding("ZZ"))

