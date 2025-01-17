'''
    Given a string in RLE format "4a2b3c" --> output the actual string --> "aaaabbccc"
'''
import itertools

def run_length_decoding(s):
    result = []
    for ele in itertools.batched(s, 2):
        result.append(int(ele[0]) * ele[1])

    return "".join(result)

def better_run_length_decoding(s):
    result = []
    so_far = 0

    for i in range(len(s)):
        if s[i].isdigit():
            so_far = so_far * 10 + int(s[i])
        else:
            result.append(s[i] * so_far)
            so_far = 0

    return "".join(result)
    

print(run_length_decoding("4a2b3c0l"))
print(better_run_length_decoding("4a2b3c0l"))