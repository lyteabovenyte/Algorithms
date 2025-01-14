'''
    suppose the keypad on phone with this mapping:
    keypad = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    you are given a phone_number, generate all the possible words that can be produced by that string
    number.
'''
import itertools

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def mnemonic_phone_number(d):
    return [
        ''.join(mnemonic) for mnemonic in itertools.product(*(MAPPING[int(digit)] for digit in d))
    ]