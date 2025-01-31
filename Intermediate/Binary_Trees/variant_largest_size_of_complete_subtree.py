"""
    Write a program which returns the size of the largest subtree that is compelete.
"""
import collections

def largest_complete_subtree(tree):
    CompleteTreeWithSize = collections.namedtuple('CompleteTreeWithSize', ('complete', 'size'))

    def compute_size(tree):
        if not tree:
            return CompleteTreeWithSize(True, -1)
        
        left_subtree = compute_size(tree.left)
        if not left_subtree.complete:
            return CompleteTreeWithSize(False, 0)
        
        right_subtree = compute_size(tree.right)
        if not right_subtree.complete:
            return CompleteTreeWithSize(False, 0)
        
        is_complete = 
