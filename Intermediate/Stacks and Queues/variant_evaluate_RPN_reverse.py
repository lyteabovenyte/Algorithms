'''
    evaluate RPN with the reverse Rule:
    except for A,B,(OP) we have (OP),A,B
'''
# NOTE: this function assumes the input is a well-formed polish notation expression
def evaluate_modified_RPN(expression: str) -> int:
    stack = []
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y,
        '*': lambda y, x: x * y, '/': lambda y, x: int(x / y)
    }

    for token in expression.split(","):
        if token in OPERATORS:
            stack.append(OPERATORS[token])
        else:
            stack.append(int(token))
        while len(stack) >= 3 and type(stack[-1]) == int and type(stack[-2]) == int:
            first_element = stack.pop()
            second_element = stack.pop()
            op = stack.pop()
            stack.append(op(first_element, second_element))
        
    return stack

print(evaluate_modified_RPN("+,*,-,3,1,5,+,44,66"))
