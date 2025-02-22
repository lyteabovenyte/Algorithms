"""
    Using disjoint_sets to find the connected components in an undirected graph.
    it's good for dynamic graphs.
"""
from typing import List, Tuple

class Info:
    def __init__(self, element):
        if element == None:
            raise ValueError(f'NoneType object is not allowed.')
        self.root = element
        self.rank = 1

class Disjoint_set:
    def __init__(self, initail_set: List):
        self._parents_map = {}
        for element in initail_set:
            if element == None or element in self._parents_map:
                raise ValueError(f'{element} cannot be NoneType object or Duplicate.')
            self._parents_map[element] = Info(element)

    def find_partition(self, element):
        info = self._parents_map[element]
        if info.root == element:
            return element
        info.root = self.find_partition(info.root) # also changing the reference to the root.
        return info.root
    
    def merge(self, element1, element2):
        r1 = self.find_partition(element1)
        r2 = self.find_partition(element2)
        if r1 == r2:
            return False
        info1 = self._parents_map[r1]
        info2 = self._parents_map[r2]
        if info1.rank > info2.rank:
            info2.root = info1.root
        elif info2.rank > info1.root:
            info1.root = info2.root
        else:
            info1.root = info2.root
            info1.rank += 1 # here rank is the height of the tree.
        return True
        # if info1.rank >= info2.rank:
        #     info2.root = info1.root
        #     info1.rank += info2.rank # here the rank is the size, not the height of the tree.
        # else:
        #     info1.root = info2.root
        #     info2.root += info1.root
        # return True

def find_connected_components(initial_nodes, edges: List[Tuple]):
    """
        takes the nodes and edges of an undirected graph
        and returns the concrete connected components.
    """
    ds = Disjoint_set(initail_set=initial_nodes)

    for u, v in edges:
        ds.merge(u, v)

    # finding all the connected components
    components = {}
    for node in initial_nodes:
        root = ds.find_partition(node)
        if root not in components:
            components[root] = []
        components[root].append(node)

    return list(components.values())


print(find_connected_components([0, 1, 2, 3, 4, 5, 6, 7], [(0, 1), (1, 2), (3, 4), (4, 5), (5, 6)]))
# returns [[0, 1, 2], [3, 4, 5, 6], [7]]