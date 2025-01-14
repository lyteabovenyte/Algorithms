'''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
import functools

# greedy algorithm!
def max_profit(a):
    i, j = 0, 1
    max_profit = 0
    while j < len(a):
        if a[i] < a[j]:
            max_profit += a[j] - a[i]
        i, j = i + 1, j + 1
    return max_profit


print(max_profit([7, 1, 5, 3, 6, 4]))

        

