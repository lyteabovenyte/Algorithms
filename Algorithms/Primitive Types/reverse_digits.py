'''
    Write a program which takes an integer and returns the integer 
    corresponding to the digits of the
    input written in reverse order.
    For example, the reverse of 42 is 24, and the reverse of -314 is -413.
'''

def reverse_digits(x):
    result = 0
    x = abs(x)   # compute for |x|, apply the sign in the end
    while x:
        result = (result * 10) + (x % 10)
        x //= 10
    return -result if x < 0 else result

print(reverse_digits(2467))
