'''
    Self implemented stack with auxiliary stack to store the max value.
'''
from collections import namedtuple
class Stack:

    # auxiliary stack to record the max and it's occurence.
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._elements = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._elements) == 0

    def max(self):
        if self.empty():
            raise IndexError("max(): empty stack")       
        return self._cached_max_with_count[-1].max

    def pop(self):
        if self.empty():
            raise IndexError("pop(): empty stack")
        pop_element = self._elements.pop()
        current_max = self._cached_max_with_count[-1].max
        if current_max == pop_element:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count == 0:
                self._cached_max_with_count.pop()
        return pop_element
    
    def push(self, x):
        self._elements.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))
