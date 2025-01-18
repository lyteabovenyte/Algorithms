'''
    Given two string s(the search string) and t (the text) find the first occurence of s in t.
'''
import itertools

# this is my solution but there are some well-known
# string matching algorithms with linear-time time complexity.
def search_string(t, s):
    
    # first examine the lenght of the substring
    sub_length = len(s)
    for i in range(len(t)):
        if "".join(tuple(itertools.islice(t[i:], sub_length))) == s:
            return i
    return False


# returns the start of the substring index i.e 4.
print(search_string("lyteabovenyte", "nyte")) 

'''
the popular string matching algorithms are
KMP, Boyer-Moore and Rabin-Krap
below is the Rabin-Krap algorithm for string matching
for this, we need a good additive hash function to 
compute the so called "fingerprint" of each substring
'''
import functools

def rabin_krap(t, s):
    if len(s) > len(t):
        return -1 # s cannot be a substring of t
    
    BASE = 26
    # hash codes for the substring of t and s
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE ** max(len(s) - 1, 0) # BASE ^ |s - 1|, used for rolling update

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s): i] == s:
            return i - len(s)  # found a match
        
        # using rolling update to compute the hash code.
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    # Tries to match s and t[-len(s):]
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1  # s is not a substring of t.


print(rabin_krap("lyteabovenyte", "nyte"))