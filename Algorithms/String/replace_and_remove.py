'''
    Given an array and a k. apply the rules provided below at most k times.
    1) delete each 'a' and replace it with two 'd'
    2) delete each 'b'.
'''

def apply_rules(arr, k):
    for i, ele in enumerate(arr):
        if ele == "a" and k > 0:
            arr.insert(i+1, "d")
            arr[i] = "d"
            k -= 1
        if ele == "b" and k > 0:
            del arr[i]
            k -= 1

def replace_and_remove(size, s):
    # forward iteration: remove 'b's and count the number of 'a's
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == "a":
            a_count += 1
    
    # backward iteration: replace 'a's with 'dd's starting from the end.
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == "a":
            s[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -= 1
        else:
            s[cur_idx] = s[write_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


print(apply_rules(["a", "b", "a", "c", "a", "d", "b"], 2))
