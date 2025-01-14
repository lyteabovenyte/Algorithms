'''
Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible
for every character of str1 to every character of str2.
And all occurrences of every character in 'str1' map to the same character in 'str2'.

    foo, bar --> False
    foo, bee --> True
    fow, bee --> False

'''


def isomorphic(str1, str2):
    dict = {}
    set_values = set()
    
    if len(str1) != len(str2):
        return False
    
    i = 0
    for ch1 in str1:
        key_existance = dict.get(ch1, None)
        if key_existance:
            if dict[ch1] != str2[i]:
                return False
            else:
                dict[ch1] = str2[i]
                set_values.add(str2[i])
                i += 1
        else:
            if str2[i] in set_values:
                return False
            else:
                dict[ch1] = str2[i]
                set_values.add(str2[i])
                i += 1
            
    return True 


#another try, 2 weeks later :) 
def isomorphic2(str1, str2):
    dict_value = {}
    set_values = set()
    
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        key_existance = dict_value.get(str1[i], None)
        if key_existance:
            if key_existance != str2[i]:
                return False
        else:
            if str2[i] not in set_values:
                dict_value[str1[i]] = str2[i]
                set_values.add(str2[i])
            else:
                return False
    
    return True


print( isomorphic2 ('fow', 'bee') )