'''
    Given a set of buildings, return each building which has sunset_view.
    the building which has sunset_view is a building that doesn't have any taller building
    to it's east (right).
'''
from collections import namedtuple

def sunset_view(seq):
    BuildingWithHeight = namedtuple("BuildingWithHeight", ("id", "height"))

    candidates = [] # Stack
    for building_idx, building_height in enumerate(seq):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [candidate.height for candidate in reversed(candidates)]

print(sunset_view([3, 6, 2, 7, 9, 5, 1, 2]))