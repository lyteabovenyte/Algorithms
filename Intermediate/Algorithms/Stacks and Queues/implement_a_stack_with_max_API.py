from collections import namedtuple

class Stack:
    ElementsWithCachedMax = namedtuple('ElementsWithCachedMax', ('element', 'max'))
    
    '''
        Design a stack that includes a max operatoins, in addition to push and pop. The 
        max method should return the maximum value stored in the stack. 
    '''
    
    def __init__(self):
        self._elements_with_cached_max = []
        
        
    def is_empty(self):
        return len(self._elements_with_cached_max) == 0
    
    
    def max(self):
        if self.is_empty():
            raise IndexError('max(): empty stack')
        return self._elements_with_cached_max[-1].max
    
    
    def pop(self):
        if self.is_empty():
            raise IndexError('pop(): empty stack')
        return self._elements_with_cached_max.pop().element
    
    
    def push(self, value):
        self._elements_with_cached_max.append(
            self.ElementsWithCachedMax(value, value if self.is_empty() else max(
                value, self.max()
            ))
        )