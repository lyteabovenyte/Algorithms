'''
    Given an integer n, return the Look_and_say of the nth integer in the string format.
    look_and_say game --> 1 --> one 1 --> 11
                          11 --> two 1 --> 21
                          21 --> one 2, one 1 --> 1211
                          1211 --> one 1, one 2, two 1 --> 111221
                          ...
'''
import itertools

def look_and_say(n):
    seq = ['1']
    i = 1
    while n >= i:
        digit = seq[-1]
        c, prev, partial_seq = 1, -1, []
        for ele in digit:
            if ele == prev:
                c += 1
            else:
                partial_seq.extend([c, prev])
                prev = ele
                c = 1
        partial_seq.extend([c, prev]) # the last element
        seq.append("".join(list(str(item) for item in partial_seq[2:])))
        i += 1
    return seq[-1]


print(look_and_say(4))
        

# trying to improve
def look_and_say2(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i + 1] == s[i]:
                count += 1
                i += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)
    
    s = '1'
    for i in range(1, n):
        s = next_number(s)
    return s

print(look_and_say2(5))

# wow approach
def wow_look_and_say(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s)
        )
    return s

print(wow_look_and_say(5))