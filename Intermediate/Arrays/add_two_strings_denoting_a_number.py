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

print(add_array("99", "101"))