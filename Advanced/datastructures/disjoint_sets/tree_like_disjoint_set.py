"""
    Changing the initial disjoint_set to be tree-like rather arrays or set to represent each partition.
"""
from typing import List

class TreeDisjoint_set:
    def __init__(self, initial_set: List):
        """
            Constructing the TreeDisjoint_set.
        """
        self._parents_map = {}
        for element in initial_set:
            if element == None or element in self._parents_map:
                raise ValueError(f'NoneType object or Duplicate is not allowed. {element}')
            # each element initially is it's own parent.
            self._parents_map[element] = element

    def find_partition(self, element):
        """
            find_partition takes an element and returns another element,
            the one at the root of the tree for the partition for which
            element belongs.
        """
        if element == None or element not in self._parents_map:
            raise ValueError(f'{element} not found or is NoneType object.')
        parent = self._parents_map[element]
        if parent != element:
            parent = self.find_partition(parent) # climb up to the root of the tree.
        return parent # retuning the root of the tree (Partition)
    
    def merge(self, element1, element2):
        """
            takes two elements, and merges their partition if and only if
            their partitions differ.
            we simply get boot roots and set one's root to be the parent
            of the other's root.
        """
        p1 = self._parents_map[element1]
        p2 = self._parents_map[element2]
        if p1 == p2:
            # already in same partition
            return False
        # otherwise, we set the parent of p2 to be the parent of p1.
        self._parents_map[p2] = p1

    