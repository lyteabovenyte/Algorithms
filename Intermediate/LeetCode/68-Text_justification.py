"""
    https://leetcode.com/problems/text-justification
    level: Hard
"""
def my_sol(words, maxWidth):
    res = []
    stack, stack_len = [], 0
    for ele in words:
        stack.append(ele)
        stack_len += len(ele) + 1
        if stack_len > maxWidth:
            ele = stack.pop()
            stack_len, stack_count = sum([len(ele) for ele in stack]), len(stack)
            if len(stack) == 1:
                res.append(("".join(stack).ljust(maxWidth)))
            else:
                # handle spaces between the words
                d = maxWidth - stack_len
                while d > 0:
                    for i in range(len(stack) - 1):
                        stack[i] += " "
                        d -= 1
                        if d <= 0:
                            break
                res.append("".join(stack))
            stack, stack_len = [ele], len(ele)

    res.append((" ".join(stack).ljust(maxWidth)))

    return res

print(my_sol(["This", "is", "an", "example", "of", "text", "justification."], 16))

# ------------------------

def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    ans = []
    row = []
    rowLetters = 0
    for word in words:
      if rowLetters + len(word) + len(row) > maxWidth:
        for i in range(maxWidth - rowLetters):
          row[i % (len(row) - 1 or 1)] += ' '
        ans.append(''.join(row))
        row = []
        rowLetters = 0
      row.append(word)
      rowLetters += len(word)

    return ans + [' '.join(row).ljust(maxWidth)]

print(fullJustify(["Listen","to","many,","speak","to","a","few."], 6))
