'''
    Given an integer, return the shortest valid roman number representing that integer
'''
from collections import OrderedDict

def integer_to_roman(n):

    # using OrderedDict to traverse downward.
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(n):
        for r in roman.keys():
            x, y = divmod(n, r)
            yield roman[r] * x
            n = y
            if n <= 0:
                break

    return ''.join([a for a in roman_num(n)])

print(integer_to_roman(3549))