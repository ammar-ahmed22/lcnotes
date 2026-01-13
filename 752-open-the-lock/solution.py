from typing import List
from collections import deque

class Solution:
    def combo2int(self, combo: str) -> List[int]:
        return [int(c) for c in combo]

    def int2combo(self, arr: List[int]) -> str:
        return "".join([str(n) for n in arr])

    def neighbours(self, combo: str) -> List[str]:
        result = []
        for i in range(len(combo)):
            up_n = self.combo2int(combo)
            down_n = self.combo2int(combo)
            up_n[i] = (up_n[i] + 1) % 10
            down_n[i] = (down_n[i] - 1) % 10
            result.append(self.int2combo(up_n))
            result.append(self.int2combo(down_n))
        return result
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"

        if start in dead:
            return -1
        if start == target:
            return 0
        q = deque([(start, 0)])
        visited = { start }

        while q:
            curr, turns = q.popleft()
            for n in self.neighbours(curr):
                if n in dead or n in visited:
                    continue
                if n == target:
                    return turns + 1
                q.append((n, turns + 1))
                visited.add(n)
        return -1



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
