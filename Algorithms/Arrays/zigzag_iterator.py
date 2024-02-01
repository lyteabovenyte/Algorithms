'''
ZigZag iterator in queues:

    [1, 3, 5, 7], [2, 4, 6, 8] --> 1 2 3 4 5 6 7 8

'''


#Function based solution
def zig_zag(arr1, arr2):
    l = []
    for ele1, ele2 in zip(arr1, arr2):
        l.append(ele1)
        l.append(ele2)
        
    return l


# for ele in zig_zag([1, 3, 5, 7], [2, 4, 6, 8]):
#     print(ele, end=' ')


# class based solution
class ZigZag:
    
    def __init__(self, arr1, arr2):
        self.queue = [arr1, arr2]
        
        
    def next(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r
    
    
    def has_next(self):
        if self.queue:
            return True
        return False
    

# z = ZigZag([1, 3, 5, 7], [2, 4, 6, 8])

# while z.has_next():
#     print(z.next(), end=" ")
