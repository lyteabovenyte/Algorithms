"""
    Often data is almost sorted. for example a server receives timestamped stock quotes and earlier quotes may arrive slightly 
    after later quotes becuase of the difference in server loads and network routes. let's address effiecient ways to sort
    such data.

    Design an algorithm with takes as input a very long sequence of numbers and print the numbers in sorted order. Each number
    is at most k away form its correctly sorted position. (such an array is sometimes referred to as being k-sorted). e.g, no
    number in the sequence [3, -1, 2, 6, 4, 5, 8] is more than 2 away from its final sorted position.
"""
import heapq


def my_sol(seq, k):
    min_heap = seq[:k]
    heapq.heapify(min_heap)
    result = []
    result.append(heapq.heappop(min_heap))


    for ele in seq[k:]:
        item = heapq.heappushpop(min_heap, ele)
        result.append(item)

    result.append(heapq.heappop(min_heap))
    result.append(heapq.heappop(min_heap))
    return result

print(my_sol([3, -1, 2, 6, 4, 5, 8], 3))

# --- More readable and pythonic way of doing ---
import itertools

def pythonic(seq, k):
    result = []
    min_heap = []
    
    for x in itertools.islice(seq, k):
        heapq.heappush(min_heap, x)

    for x in seq[k:]:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # seq is finished, so we start popping from heap (Min_heap)
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

print(pythonic([3, -1, 2, 6, 4, 5, 8], 3))