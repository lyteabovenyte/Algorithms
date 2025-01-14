'''
    Given a string denoting a specific positive number in base b1, convert it to a string denoting the number in
    base b2. inputs --> string, b1, b2
'''
import functools
import string 

table = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}

# helper function.
def convert_base_to_ten(s, base):
    return functools.reduce(
        lambda running_sum, c: running_sum * base + string.digits.index(c),
        s, 0
    )

# helper function
def convert_ten_to_base(d, base):

    res = []
    while d > base:
        res.append(d % base)
        d //= base

    res.append(d)
    
    result = []
    for ele in res:
        if ele > 9:
            result.append(str(table[ele]))
        else:
            result.append(str(ele))

    final_result = "".join(reversed(result))
    return final_result

# main logic goes here.
def main(s, b1, b2):
    source_integer = convert_base_to_ten(s, b1)
    dest = convert_ten_to_base(source_integer, b2)
    return dest

print(main("615", 7, 13))

# approach number 2

def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return('' if num_as_int == 0 else
               construct_from_base(num_as_int // base, base) + 
               string.hexdigits[num_as_int % base].upper())
    
    is_negative = num_as_string[0] == "-"
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0
    )
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


print(convert_base("615", 7, 13))
