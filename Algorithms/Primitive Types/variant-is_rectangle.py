'''
    Given four points in the plane, how would we check if they form a rectangle?
'''
from operator import attrgetter
import collections
import math

Point = collections.namedtuple("Point", ('x', 'y'))

# the length of the vector from Pa -> Pb
def vec(Pa, Pb):
    return math.sqrt(abs(Pa.x - Pb.x) ** 2 + abs(Pa.y - Pb.y) ** 2)

def is_rectangle(lst):
    
    # first we sort the lst clockwise based on the minimum 'y'
    sorted_lst = sorted(lst, key=attrgetter('y'))

    # then we calculate the diagonal, if equal -> True else -> False
    if vec(sorted_lst[0], sorted_lst[2]) == vec(sorted_lst[1], sorted_lst[3]):
        return True
    return False

        
P1 = Point(1, 2)
P2 = Point(3, 1)
P3 = Point(2, 4)
P4 = Point(4, 3)
lst = [P1, P2, P3, P4]

print(is_rectangle(lst))

    
