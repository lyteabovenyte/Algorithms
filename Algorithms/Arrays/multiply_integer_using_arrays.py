'''
    Given two arrays denoting integers, return their product.
    [2, 3], [1, 2] --> return [2, 8, 6]
'''

def multiply_arrays(s, t):
    # defining helper function to add
    def add_array(a, b):
        running_sum = 0
        result = []
        j = max(len(a), len(b)) - 1
        while j >= 0:
            w = a[j] + b[j] + running_sum
            running_sum = 0
            if w > 9:
                running_sum += 1
                w = w % 10
            result.insert(j, w)
            j -= 1
        if running_sum != 0:
            result.insert(0, 1)
        return result
    
    def multiply(l, b): # l --> list, b --> number
        running_sum = 0
        result = []
        j = len(l) - 1
        while j >= 0:
            w = l[j] * b + running_sum
            running_sum = 0
            if w > 9:
                running_sum += 1
                w = w % 10
            result.insert(j, w)
            j -= 1
        if running_sum != 0:
            result.insert(0, 1)
        return result

    final = 0
    i = 0
    for k in reversed(range(len(t) - 1)):
        res = multiply(s, t[k])
        res.append(0 * i)
        i += 1
        final = add_array([final], res)

    return final


def add_array(a, b):
        running_sum = 0
        result = []
        j = max(len(a), len(b)) - 1
        while j >= 0:
            w = a[j] + b[j] + running_sum
            running_sum = 0
            if w > 9:
                running_sum += 1
                w = w % 10
            result.insert(j, w)
            j -= 1
        if running_sum != 0:
            result.insert(0, 1)
        return result

# we can use * to multiply.
def final_try(s, t):
    result = []
    i = 0    # s and t are two arrays, denoting a specific number.
    for j in reversed(range(len(t))):
        w = s * t[j] * (10 * i)
        result = add_array(result, w)


print(multiply_arrays([9, 9], [9, 9]))
            