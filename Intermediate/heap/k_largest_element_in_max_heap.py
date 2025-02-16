"""
    heaps have partial ordering, unlinke sorted array or a balanced BST.
    Design an algorithm which gets a max_heap represented as an array, and return the k largest element in the max_heap
    provided.
"""
import heapq

def compute_k_largest_element(a, k):
    if k <= 0:
        return []
    
    # using a max_heap to store elements from a with initial element of the root and it's index.
    # then iteratively process the childrens
    candidate_max_heap, result = [], []
    candidate_max_heap.append((-a[0], 0)) 
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(a): # it means we have left child for this node.
            heapq.heappush(candidate_max_heap, (-a[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(a):
            heapq.heappush(candidate_max_heap, (-a[right_child_idx], right_child_idx))
    return result

print(compute_k_largest_element([561, 314, 401, 28, 156, 359, 271, 11, 3], 4))