"""
    The core implementation of Disjoint Sets and it's APIs.
"""
from typing import List

class Disjoint_Set:
    def __init__(self, initial_set: List):
        """ 
            Construction.
            Just take care of allocation of the basic fields needed
            by the class and assigns each element to its own partition.
            it takes an initial set of elements and initialize the
            disjoint set with an empty set.
        """
        # Associative array to index elements and map them to their respective partitions.
        self._partitions_map = {}
        for element in initial_set:
            if element == None or element in self._partitions_map:
                raise ValueError(f'NoneType object or Duplicate is not allowed. {element}')
            self._partitions_map[element] = set(element)

    def __sizeof__(self, element):
        return len(self._partitions_map[element])
    
    def add(self, new_element):
        """
            Adds a new element to the disjoint set.
            returns True if and only if the new element
            hass been successfully added to the disjoint set.
        """
        if new_element == None or new_element in self._partitions_map:
            raise ValueError(f'Element cannot be NoneType object or Duplicate. {new_element}')
        self._partitions_map[new_element] = set(new_element)
        return True

    def find_partition(self, element):
        """
            find_partition checks that the element is valid
            and then returns the set which element is associated with.
        """
        if element == None or element not in self._partitions_map:
            raise ValueError(f'{element} is not in set or a NoneType object')
        return self._partitions_map[element]

    def are_disjoint(self, element1, element2):
        """
            are_disjoint takes two elements and returns True
            if and only if the elements are valid but don't belong
            to the same partition
        """
        p1 = self.find_partition(element1)
        p2 = self.find_partition(element2)
        return p1 != p2

    def same_partition(self, element1, element2):
        """
            same_partition returns True if and only if the
            elements are valid and belongs to the same partition.
        """
        p1 = self.find_partition(element1)
        p2 = self.find_partition(element2)
        return p1 == p2

    def merge(self, element1, element2):
        """
            merge takes two elements, merges their partitions,
            and return True if and only if the two elements
            were in the two different partitions that now
            are merged or False if there were already in
            the same partition.
        """
        p1 = self.find_partition(element1)
        p2 = self.find_partition(element2)
        if p1 == p2:
            return False
        # adding elements from smaller set to the larger one.
        if self.__sizeof__(element1) > self.__sizeof__(element2):
            for element in p2:
                p1.add(element)
                self._partitions_map[element] = p1
        else:
            for element in p1:
                p2.add(element)
                self._partitions_map[element] = p2
        return True