'''
    Given a string such as "aaaabcccaa" return the RLE --> "4a1b3c2a"
'''
def run_length_encoding(s):
    
    result = []
    prev = ""
    count = 0

    for ele in s:

        if ele == prev:
            count += 1
        else:
            result.append(str(count) + prev)
            prev = ele
            count = 1

    # adding last_one
    result.append(str(count) + prev)
    return "".join(result[1:])


print(run_length_encoding("aaaabcca"))