'''
    Give the corresponding spreadsheet column by the given integer
    4 --> 'D', 27 --> 'AA'
'''
import string

def variant_spreadsheet(d):

    # num as int is in base 10.
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) + 
                string.hexdigits[num_as_int % base].upper())
    
    ob = str(construct_from_base(d, 26))
    res = []
    for ele in ob:
        res.append(chr(int(ele) + 64))
    
    return "".join(res)


print(variant_spreadsheet(27))
    



    
