"""
    https://leetcode.com/problems/valid-palindrome
"""

def pali(s: str):
    s = "".join([ele.lower() for ele in s if ele.isalnum()])
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True

print(pali("A man, a plan, a canal: Panama"))
print(pali("race a car"))
