"""
    Design an O(n logk) time algorithm that reads a sequence of n elements and for each element, starting
    from the kth element, prints the kth largest element read up to that point. the length of the sequence is not know
    in advance. Your algorithm cannot use more than O(k) additional storage. what is the worst-case inputs for your algorithm?
"""
import heapq

# this algo uses O(n) additional space.
def kth_largest_element_up_to_n(a, k):
    min_heap, result = [], {}

    for item in a[:k]:
        heapq.heappush(min_heap, item)

    for ele in a[k:]:
        res = heapq.nlargest(k, min_heap)[1]
        result[ele] = res
        heapq.heappush(min_heap, ele)

    return result

# for each element returns the kth largest up to that element.
print(kth_largest_element_up_to_n([2, 0, 1, 4, 6, 5, 9, 10], 2)) # {1: 0, 4: 1, 6: 2, 5: 4, 9: 5, 10: 6}

print("-----")

def lower_space_complexity(seq, k):
    result, min_heap = {}, []

    for i, ele in enumerate(seq):
        if i >= k - 1:
            result[ele] = min_heap[0]

        if i < k:
            heapq.heappush(min_heap, ele)
        else:
            if ele > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, ele)
        
    return result

print(lower_space_complexity([2, 0, 1, 4, 6, 5, 9, 10], 2))