"""
    https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
    - how would you implement the `find()` method in python?
"""

def find(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


print(find("lyteabovenyte", "above"))
print(find("leetcode", "leeto"))