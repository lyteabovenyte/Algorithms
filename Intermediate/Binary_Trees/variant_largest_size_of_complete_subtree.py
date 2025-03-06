"""
    Write a program which returns the size of the largest subtree that is compelete.
"""
import collections

def largest_complete_subtree(tree):
    CompleteTreeWithSize = collections.namedtuple('CompleteTreeWithSize', ('complete', 'size'))