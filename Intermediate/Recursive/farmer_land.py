'''
    Suppose you’re a farmer with a plot of land.
    You want to divide this farm evenly into square plots. You want the plots
    to be as big as possible.
    
    How do you figure out the largest square size you can use for a plot of
    land?
    
'''

def divide_farm_land(x, y):
    if y > x:
        x, y = y, x
        
    x = x % y
    
    if ( x != 0):
        return divide_farm_land(x, y)
    else:
        return y
    
    
print( divide_farm_land(45, 12) ) # --> outputs 3