'''
    just a file for testing my thoughts :D. ignore this.
'''

import string
import functools

def convert_base(num_as_str, b1, b2):
    
    def construct_to_base(num, base):
        return ('' if num == 0 else
                construct_to_base( num // base, base) + 
                string.hexdigits[num % base].upper())
        
        
    is_negative = num_as_str[0] == '-'
    
    #converting the num_as_as in base b1, to num_as_int in base 10, a normal integer
    num_as_int = functools.reduce(
        lambda running_sum, c: running_sum * b1 + string.hexdigits.index(c.lower()), 
        num_as_str[is_negative:], 0
    )
    
    
    
    
def construct_to_base(num, base):
        return ('' if num == 0 else
                construct_to_base( num // base, base) + 
                string.hexdigits[num % base].upper())
        


print( type(construct_to_base(123, 7)) )    
    
