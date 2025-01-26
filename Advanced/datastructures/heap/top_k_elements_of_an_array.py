'''
    Imagine you are given an array of billions of billions(n) entries, an you want to get the top thousands(k) of them
    you can:
    1. Sort them and get the top k elements --> O(nlogn)
    2. selecting the top elements one by one k times --> O(n * k)
    3. or you can use e min heap that has the capacity of exactly k, each time you get and element
    which is greater than the top of the heap, you extract the top and insert that element into the heap.
    in this way you always have the k largest elements in partial ordering --> O(n + klogk)
'''
from dway_heap import DWayHeap

def k_largest_element(A, k):
    # we should use the inverse of the elements
    # cause DWayHeap is a max_heap
    A = list(map(lambda ele: -ele, A))
    heap = DWayHeap() 
    for ele in A:
        if (heap.__sizeof__ == k and heap.peek() < ele):
            heap.top()
            if heap.__sizeof__ < k :
                heap.insert(ele)
    
    return heap