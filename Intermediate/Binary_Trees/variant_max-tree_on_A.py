"""
    Given an array of distinct integers, let the index of the max element of A be m,
    Define the max-tree of A to be the binary tree on the entries of A which the root contains the max element
    and it's left child be the max-tree on A[0, m - 1] and right child be the max-tree on A[m + 1, n - 1].
    Design an O(n) algorithm for building the max-tree of A.

    Algorithm recap:
    - We process elements one by one.
    - Maintain a monotonic decreasing stack (i.e., elements in decreasing order).
    - For each element:
        - Pop elements from the stack until we find a larger element.
        - The last popped element becomes the left child.
        - The remaining top element in the stack (if any) becomes the parent.
"""
from BinaryTreeNode import BinaryTreeNode as Btn
from typing import List, Optional

# Time complexity: O(n)
def construct_max_tree(A):
    stack = []
    nodes_map = {}

    for ele in A:
        curr = Btn(ele)
        nodes_map[ele] = curr

        while stack and stack[-1].data < ele:
            popped = stack.pop()
            curr.left = popped

        if stack:
            stack[-1].right = curr

        stack.append(curr)
    return stack[0] # root is the first element remaining in the stack

# Time complexity: O(n^2)
def constructMaxTreeRecursive(nums: List[int]) -> Optional[Btn]:
    if not nums:
        return None

    # Find index of max element
    max_index = nums.index(max(nums))

    # Create root node
    root = Btn(nums[max_index])

    # Recursively construct left and right subtrees
    root.left = constructMaxTreeRecursive(nums[:max_index])
    root.right = constructMaxTreeRecursive(nums[max_index + 1:])

    return root