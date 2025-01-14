'''
    write a program that takes an array denoting the daily stock price,
    and returns the maximum profit that could be made by buying and then selling one share of that stock.

'''
#O(n^2) Time complexity
def buy_and_sell_stock_once(arr):
    max_profit = 0 
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) > max_profit:
                max_profit = arr[j] - arr[i]
                
    return max_profit



#another implementation with O(n) Time complexity
def buy_and_sell_stock_once2(arr):
    '''
        min_val: minimum value so far in the array.(before the ith element)
    '''
    max_profit = 0
    min_val = float('inf')
    for i in range(len(arr)):
        if arr[i] - min_val > max_profit:
            max_profit = arr[i] - min_val
        if arr[i] < min_val:
            min_val = arr[i]
    return max_profit



#or
def buy_and_sell_stock_once3(arr):
    min_price_so_far, max_profit = float('inf'), 0
    for price in arr:
        max_profit_so_far = price - min_price_so_far
        max_profit = max(max_profit_so_far, max_profit)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit 
    



print( buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) )
print(buy_and_sell_stock_once2([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
print(buy_and_sell_stock_once3([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))