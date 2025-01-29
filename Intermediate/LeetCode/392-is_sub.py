"""
    https://leetcode.com/problems/is-subsequence
"""

def is_sub(s: str, t: str):
    ps, pt = 0, 0
    while ps < len(s) and pt < len(t):
        if s[ps] == t[pt]:
            ps += 1
        pt += 1
    return ps == len(s)


print(is_sub("abc", "abfkjdhfc"))