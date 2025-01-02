'''
    Given an array of boolean-valued keys, reorder them in such a way that False values appear first.
'''

def partitoning_boolean_keyed_values(l):
    i, j = 0, len(l) - 1
    while i < j:
        if l[i] == True:
            l[i], l[j] = l[j], l[i]
            j -= 1
        else:
            i += 1
    return l


print(partitoning_boolean_keyed_values([True, False, True, True, False, False, True, False]))
        


        
