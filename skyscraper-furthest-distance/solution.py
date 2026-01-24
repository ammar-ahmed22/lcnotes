from typing import List
import heapq

class Solution:
    def furthestDistance(self, heights: List[int], springs: int, sandbags: int) -> int:
        # Optimal (min heap, O(n log n) time, O(n) space)
        max_heap = []
        # O(n)
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            sandbags -= diff
            # O(log n)
            heapq.heappush(max_heap, -diff)

            if sandbags < 0:
                if springs == 0:
                    return i
                springs -= 1
                # O(log n)
                sandbags += -heapq.heappop(max_heap)
        return len(heights) - 1

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
