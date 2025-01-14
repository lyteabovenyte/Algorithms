'''
    Given an array of characters, the character can be digits, letters, blanks and punctuation,
    return the telex_encoding of the array. (punctuations are spelled out)
'''

table = {
    "!": "EXCLAIMATION MARK",
    "?": "QUESTION MARK",
    ".": "DOT",
    ",": "COMMA",
}

# TODO!!
# filling array from the front is time consuming, 
# so we try to make it happen from the back.
def telex_encoding(s):
    # first we try to count the final_result's size
    write_index = 0
    for i, ele in enumerate(s):
        if ele not in table:
            write_index += 1
        else:
            write_index += len(table[ele])

        
    size = write_index # size of the final_array.

    diff = size - len(s)
    s.extend([0] * diff) # now we fix the size of the array to be filled

    cur_write = size - 1
    cur_read = len(s) - 1

    while cur_write >= 0:
        if cur_read not in table:
            s[cur_write] = s[cur_read]
            cur_read, cur_write = cur_read - 1, cur_write - 1
        else:
            s[cur_write - len(table[s[cur_read]]) + 1: cur_write + 1] = list(table[s[cur_read]]) #!!
            cur_write -= len(table[s[cur_read]]) #!!
            cur_read -= 1

    return s
 

def telex_encoding_one_shot(s):
    write_index = 0
    for i, ele in enumerate(s):
        if ele not in table:
            s[write_index] = ele
            write_index += 1
        else:
            s[write_index] = table[ele]
            write_index += 1

    return s

print(telex_encoding_one_shot(["a", 4, "c", ",", 2, 1]))

# print(telex_encoding(["a", 4, "c", ",", 2, 1]))
