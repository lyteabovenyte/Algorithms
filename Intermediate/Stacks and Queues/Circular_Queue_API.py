"""
    Implementing a Queue API using an array for storing elements.
    Our API includes a constructor function, which takes as argument the initial capacity of the queue,
    enqueue and dequeue functions and a function which returns the number of elements stored.
    Implementing dynamic resizing to support storing an arbitrary large number of elements.
"""
# Circular behavior in Queues
class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries):  # Resize is needed
            # Makes the queue elements appear consecutively
            self._entries = (
                self._entries[self._head:] + self._entries[:self._tail]
            )
            # Reset head and tail
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (
                len(self._entries) * Queue.SCALE_FACTOR - len(self._entries)
            )

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries) # Circular behavior
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError("empty queue.")
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret

    def size(self):
        return self._num_queue_elements