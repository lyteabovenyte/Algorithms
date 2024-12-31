'''
    Write a Program which tests if two rectangles have a nonempty intersection. If the intersection is
    nonempty, retum the rectangle formed by their intersection.
    sol:
    at first we should get the x's and y's of the rectangles
    such as for rectangle A we get: (2, 6), (3, 5); the former
    is the x's points and the latter is the y's points.
'''
# time complexity: O(1), since the number of operation is constant.
import collections

# with imagination that the width and height are always nonnegative
Rec = collections.namedtuple('Rec', ('x', 'y', 'width', 'height'))

def rectangle_intersection(R1, R2):
    def is_intersect(R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)

    if not is_intersect(R1, R2):
        return Rec(0, 0, -1, -1) # no intersection
    
    return Rec(
            max(R1.x, R2.x),
            max(R1.y, R2.y),
            min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
            min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)
            )


R1 = Rec(2, 6, 3, 2)
R2 = Rec(3, 5, 2, 2)
print(rectangle_intersection(R1, R2))
