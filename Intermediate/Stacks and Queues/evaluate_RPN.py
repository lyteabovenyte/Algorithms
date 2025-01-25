def evaluate(expression: str) -> int:
    # if we have valid and ordered RPN.
    stack = []
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y,
        '*': lambda y, x: x * y, '/': lambda y, x: int(x / y)
    }

    for ele in expression.split(","):
        stack.append(ele)

    first_element = stack.pop(0)
    while stack:
        second_element = stack.pop(0)
        op = OPERATORS[stack.pop(0)]
        first_element = op(int(second_element), int(first_element))
    
    return first_element

print(evaluate("3,4,+,2,*,1,+,2,*"))

# more belnded expression version.
def evaluate2(expression: str) -> int:
    intermediate_result = []
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y,
        '*': lambda y, x: x * y, '/': lambda y, x: int(x / y)
    }

    for token in expression.split(","):
        if token in OPERATORS:
            intermediate_result.append(OPERATORS[token](
                intermediate_result.pop(), intermediate_result.pop()
            ))
        else: # token is an integer
            intermediate_result.append(int(token))
    return intermediate_result[-1]

print(evaluate2("11,8,10,*,+,7,12,*,+,12,7,*,+,9,14,*,+,17,+"))
