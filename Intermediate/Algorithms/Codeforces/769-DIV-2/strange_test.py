'''
    https://codeforces.com/contest/1632/problem/C

    approach: first we examine the minimum value of a|b --> the first number which is a power of which is less
    than or equal to a and b.
    i.e a = 2 and b = 5 --> a = 2 and b = 4 --> in this case a|b is greater or equal to 6.
    then we substract 6 to b which is 1 and it's greater than b-a which is 3, so we a:=a|b
    and then we apply b++ by a-b times
'''

tt = int(input())

while tt > 0:

    lst = list(map(int, input().rstrip().split()))
    a = lst[0]
    b = lst[1]
    # m, n = 1, 1
    # while (m * 2 < a):
    #     m *= 2
    # while (n * 2 < b): 
    #     n *= 2
    
    # # we get the least value of a|b
    # if m == n:
    #     lsb = m
    # else:
    #     lsb = m + n
    
    m = a | b
    if m - b < b - a:
        print(m - b + 1)
    else:
        print(b - a)



    # if lsb - b > b - a:
    #     print(b - a)
    # else:
    #     a = a | b
    #     print(a - b + 1)
    
    tt -= 1