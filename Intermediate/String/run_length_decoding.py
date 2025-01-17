'''
    Given a string in RLE format "4a2b3c" --> output the actual string --> "aaaabbccc"
'''
import itertools

def run_length_decoding(s):
    result = []
    for ele in itertools.batched(s, 2):
        result.append(int(ele[0]) * ele[1])

    return "".join(result)

print(run_length_decoding("4a2b3c0l"))