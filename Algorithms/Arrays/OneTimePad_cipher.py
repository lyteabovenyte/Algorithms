'''
    OneTimePad Cipher

'''

import random 


class OneTimePad:
    
    def encrypt(self, string):
        plain = [ord(ch) for ch in string]
        keys = []
        cipher = []
        
        for i in plain:
            k = random.randint(1, 300)
            encrypted_code = i + k
            cipher.append(encrypted_code)
            keys.append(k)
        
        return cipher, keys
    
    
    def decrypt(self, cipher, key):
        
        for ele in key:
            plain = [item-ele  for item in cipher]

        wanted = []
        for item in plain:
            wanted.append(chr(item))
        
        return wanted
