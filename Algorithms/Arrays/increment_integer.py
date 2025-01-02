'''
    Write a program that takes as an input an array of digits encoding a nonnegative decimal integer D and update
    the array to represent the integer D + 1
'''

def my_sol(l):
    j = len(l) - 1  # starting from the last digit.
    running_sum = 0
    l[-1] += 1 # adding one to the last digit and keep track of running-sum if it exceeds 9
    while j >= 0:
        w = l[j] + running_sum
        running_sum = 0
        if w > 9:
            running_sum += 1
            w = w % 10
        l[j] = w
        j -= 1
    if running_sum != 0:
        l.insert(0, running_sum)
    return l

# I think, mine was better btw.
def plus_one(l):
    l[-1] += 1
    for i in reversed(range(1, len(l))):
        if l[i] != 10: 
            break
        l[i] = 0
        l[i - 1] += 1
    if l[0] == 10:
        l[0] = 1
        l.append(0)
    return l

print(my_sol([9, 9, 9]))
print(plus_one([9, 9, 9]))
