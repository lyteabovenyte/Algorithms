"""
    https://leetcode.com/problems/reverse-words-in-a-string
"""

def reverse_words(s: str) -> str:
    s = s.lstrip().rstrip()

    s = [ele for ele in s.split(" ")]
    s = [ele for ele in s if ele not in ["", " "]]
    return " ".join(reversed(s))

print(reverse_words("a good   example"))