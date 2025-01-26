'''
    Given a string over {}, () and []. determine whether it is well-formed or not.
'''

def my_sol(expression: str) -> bool:
    stack, lookup = [], {'(': ')', '{': '}', '[': ']'}

    for token in expression: 
        if token in lookup:
            stack.append(token)
        else:
            if len(stack) == 0 and token in lookup.values():
                return False
            elif token in lookup.values() and lookup[stack[-1]] == token:
                stack.pop()

    return len(stack) == 0

print(my_sol(")a(mir{ala[]})"))

def well_formed(expression: str) -> bool:
    stack, lookup = [], {'(': ')', '{': '}', '[': ']'}

    for c in expression:
        if c in lookup:
            stack.append(c)
        elif not stack or lookup[stack.pop()] != c:
            return False
    return not stack

print(well_formed(")a(mir{ala[]})"))
