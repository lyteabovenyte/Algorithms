'''
    The basic Queue class, using composition to add a private field that references a library
    queue object.
'''
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()
    
    def max(self):
        return max(self._data)