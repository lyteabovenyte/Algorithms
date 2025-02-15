"""
    Consider coordinate system for Milky Way, in which earth is at (0, 0, 0). Model stars as points, and assume
    distances are in light years. The Milky way consists of 10^12 stars and their coordinates are stored in a file.

    Desing an algorithm that computes the k stars which are closest to earth.
"""
import heapq
import math

# Model the stars as a 3D point.
class Star:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __lt__(self, rhs):
        return self.distance < rhs.distance
    
    def find_closest_k_stars(stars, k):
        # using max_heap to store the closest k stars seen so far,
        # so we should insert negative distance for each star
        max_heap = []
        for star in stars:
            heapq.heappush(max_heap, (-star.distance, star))

            if len(max_heap) == k + 1:
                heapq.heappop(max_heap)

        # Iteratively extracting from the max_heap which yields the stars in sorted manner.
        # from furthest to closest.
        return [s[1] for s in heapq.nlargest(k, max_heap)] # this would need an extra step in sorting.