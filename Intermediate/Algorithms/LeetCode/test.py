from typing import List

 
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    start = prices[0]
    n = len(prices)
    for i in range(0, n):
        if start < prices[i]:
            max_profit += prices[i] - start
        start = prices[i]
    return max_profit