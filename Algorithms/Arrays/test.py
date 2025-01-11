# adding two strings denoting a specific integer
def add_array(s, t): # "122345", "432"
    length = max(len(s), len(t))
    lst_s = [int(ele) for ele in list(s.zfill(length))]
    lst_t = [int(ele) for ele in list(t.zfill(length))]
    running_sum = 0
    result = [0] * (length)
    for j in reversed(range(length)):
        w = lst_s[j] + lst_t[j] + running_sum
        running_sum = 0
        if w > 9:
            running_sum += 1
            w = w % 10
        result[j] = w
    if running_sum != 0:
        result.insert(0, 1)
    return result


def multiply(a, b): # b is a single digit array or a single digit number
    lst_a = [int(ele) for ele in list(a)]
    b = int(b)
    running_sum = 0
    result = [0] * (len(a))
    for j in reversed(range(len(a))):
        w = (lst_a[j] * b) + running_sum
        running_sum = 0
        if w > 9:
            running_sum += 1
            w = w % 10
        result[j] = w
    if running_sum != 0:
        result.insert(0, 1)
    return result

print(multiply("99", "20"))


# spiral_ordering


