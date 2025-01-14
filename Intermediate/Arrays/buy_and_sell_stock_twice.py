'''
    Given an array of stock prices, compute the max profit made by buying and
    selling at most twice. note that the second by must be after the first sell.
'''
# trick is to once compute the max_profit forward and once compute it
# backward
def buy_sell_twice(arr):
    max_profit_so_far, min_price_so_far = 0, float('inf')
    max_total_profit = 0
    forward_profits = [0] * len(arr)
    for i, price in enumerate(arr):
        min_price_so_far = min(min_price_so_far, price)
        max_profit_so_far = max(max_profit_so_far, price - min_price_so_far)
        forward_profits[i] = max_profit_so_far

    # going backward and compute the max_profit we can make
    # by buying and selling stock twice.
    max_price_so_far = float('-inf')
    
    for i, price in reversed(list(enumerate(arr[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + forward_profits[i - 1]
        )
    return max_total_profit

print(buy_sell_twice([260, 290, 295, 310, 295, 275]))
        