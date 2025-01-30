"""
    Implement a Queue given a library implementing a stack.
    approach: using two stacks, one for enqueue and one for dequeue.
"""

class Queue:
    def __init__(self):
        self._enq, self._deq = [], []  # Using two stacks for each API

    def enqueue(self, x):
        self._enq.append(x)

    def dequeue(self):
        if not self._deq:
            # Transfer elements in _enq to _deq
            while self._enq:
                self._deq.append(self._enq.pop())

        if not self._deq: # Stack is still empty.
            raise IndexError("empty stack")
        return self._deq.pop()