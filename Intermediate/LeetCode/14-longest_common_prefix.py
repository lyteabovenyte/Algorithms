from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    min_len = min([len(s) for s in strs])
    total = ""

    i = 0
    while i < min_len:
        prev, current = 0, 1
        while current < len(strs) and (strs[prev][i] == strs[current][i]):
            prev, current = prev + 1, current + 1
        if current == len(strs):
            total += strs[current - 1][i]
            i += 1
        else:
            return total
    return total

print(longest_common_prefix(["flight", "flower", "flow"]))
print(longest_common_prefix([""]))


