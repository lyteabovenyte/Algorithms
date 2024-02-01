"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you
past the end of the alphabet, just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""

from string import ascii_letters


def encrypt(string, key):
    alpha = ascii_letters
    result = ''
    
    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result


def decrypt(string, key):
    key *= -1
    return encrypt(string, key)


def brute_force(string):
    key = 1
    alpha = ascii_letters
    result = ''
    brute_force_data = {}
    
    while(key <= len(alpha)):
        result += decrypt(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1
    
    return brute_force_data



