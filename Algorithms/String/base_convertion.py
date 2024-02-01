'''
    write a program that perfoms base conversion. The input as a string, ab integer b1, and another integer b2.
    The string represents an integer in base b1. The output should be the string representing the integer in base b2.

'''
import functools
import string 


def convert_base(num_as_string, b1, b2):
    
    #converting a base 10 normal integer to another base number, representing in string.
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) + 
                string.hexdigits[num_as_int % base].upper())
        
        
    is_negative = num_as_string[0] == '-'
    
    #converting num_as_string to a base 10 normal integer
    num_as_int = functools.reduce(
        lambda running_sum, c: running_sum * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0
    )
    
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))
    
    
    
print(convert_base('615', 7, 13))