from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Squared distance (for small optimization)
        def distance(point: List[int]) -> float:
            x, y = point
            return x * x + y * y
        heap = []
        for point in points:
            d = distance(point)
            heapq.heappush(heap, (-d, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [p for _, p in heap]



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
