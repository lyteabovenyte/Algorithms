'''
    Popular buy and sell stock.
'''

def max_profit(arr):
    max_profit, min_seen_so_far = 0, float('inf')
    for i, ele in enumerate(arr): 
        if ele < min_seen_so_far:
            min_seen_so_far = ele
            min_ind = i
        if ele - min_seen_so_far > max_profit:
            max_profit = ele - min_seen_so_far
            indices = (min_ind, i)
    return max_profit, indices


print(max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 255]))