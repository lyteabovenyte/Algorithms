"""
    Implementation of disjoint_sets with compression path.
"""
from typing import List

class Info:
    """
        The Info class models (the info associated with) a node of the
        partitions' tree.
        to all purpose, just a container for two values:
        1. the root of the tree.
        2. the rank of the subtree rooted at the current element.
    """
    def __init__(self, element):
        if element == None:
            raise ValueError(f'Node {element} cannot be NoneType object.')
        # initially element is assigned to the singleton tree
        # rooted at the element itself
        self.root = element
        self.rank = 1


class Disjoint_set_compression_path:
    def __init__(self, initial_set: List):
        self._parents_map = {}
        for element in initial_set:
            if element == None or element in self._parents_map:
                raise ValueError(f'{element} cannot be NoneType object or Duplicate.')
            self._parents_map[element] = Info(element)

    def find_partition(self, element):
        """
            find_partition takes one element as input and returns
            another element, the one element at the root of the 
            tree for thee partition to which the element blongs.
        """
        if element == None or element not in self._parents_map:
            raise ValueError(f'{element} is NoneType object or is not in the set.')
        info = self._parents_map[element]
        if info.root == element:
            return element
        # climb up recursively to the root, and meanwhile
        # update the root link for the current element so
        # that it points to the actual root of the tree.
        info.root = self.find_partition(info.root)
        return info.root
    
    def merge(self, element1, element2):
        """
            merge takes to elements as input and merges their partitions
            if and only if the elements' partitions differ.
            return False otherwise.
        """
        r1 = self.find_partition(element1)
        r2 = self.find_partition(element2)
        if r1 == r2:
            return False
        info1 = self._parents_map[r1]
        info2 = self._parents_map[r2]
        if info1.rank >= info2.rank:
            info2.root = info1.root
            info1.rank += info2.rank # here the rank is the size, not the height of the tree.
        else:
            info1.root = info2.root
            info2.root += info1.root
        return True