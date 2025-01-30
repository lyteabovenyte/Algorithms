"""
    Implement a Queue with Max API, which returns the maximum element already in the queue.
    hint: if s is appended before b and b > s, s is never gonna be the max, cause s in removed
    before b.
"""
import collections

class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._candidates_for_max = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidates_for_max[0]:
                self._candidates_for_max.popleft()
            return result
        raise IndexError('empty queue.')


# another implementation using two Stack (stack_with_max API)
from Stack import Stack

class QueueWithMaxUsingStack:
    def __init__(self):
        self._enq = Stack()
        self._deq = Stack()

    def enqueue(self, x):
        self._enq.push(x)

    def dequeue(self):
        if self._deq.empty():
            while not self._enq.empty():
                self._deq.push(self._enq.pop())
        if not self._deq.empty():
            return self._deq.pop()
        raise IndexError("empty queue")

    def max(self):
        if not self._enq.empty():
            return self._enq.max() if self._deq.empty() else max(
                self._enq.max(), self._deq.max()
            )
        if not self._deq.empty():
            return self._deq.max()
        raise IndexError("empty queue.")


