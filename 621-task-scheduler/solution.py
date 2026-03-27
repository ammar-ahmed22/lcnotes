from typing import List
import heapq
from collections import defaultdict, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)

        cooldown_q = deque([])
        t = 0
        while max_heap or cooldown_q:
            t += 1
            if not max_heap:
                t = cooldown_q[0][1]
            else:
                count = -heapq.heappop(max_heap)
                count -= 1
                if count:
                    cooldown_q.append((count, t + n))
            if cooldown_q and cooldown_q[0][1] == t:
                heapq.heappush(max_heap, -cooldown_q.popleft()[0])
        return t

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
