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

    def __sizeof__(self):
        return len(self._partitions_map)
    
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

