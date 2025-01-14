'''
A1Z26 is very simple direct substitution cypher,
where each alphabet letter is replaced by its number in the alphabet.

'''

#Using List comprehension
def encode_cipher(str):
    return [ord(val) for val in str]


#Using Generators
def decode_cipher(arr):
    return "".join((chr(val) for val in arr))