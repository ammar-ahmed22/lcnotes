from typing import List
from collections import deque

class Solution:
    def neighbours(self, combo: str) -> List[str]:
        result = []
        for i in range(len(combo)):
            up_n = [int(c) for c in combo]
            down_n = [int(c) for c in combo]
            up_n[i] = (up_n[i] + 1) % 10
            down_n[i] = (down_n[i] - 1) % 10
            result.append("".join([str(n) for n in up_n]))
            result.append("".join([str(n) for n in down_n]))
        return result

    def minLockTurns(self, start: str, target: str, blocked: List[str]) -> int:
        block = set(blocked)
        if start in block:
            return -1
        if start == target:
            return 0

        q = deque([(start, 0)])
        visited = { start }
        while q:
            curr, turns = q.popleft()
            for n in self.neighbours(curr):
                if n in visited or n in block:
                    continue
                if n == target:
                    return turns + 1
                visited.add(n)
                q.append((n, turns + 1))
        return -1

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
