from typing import List, Tuple
from collections import deque

class Solution:
    def neighbours(self, coord: Tuple[int, int], grid: List[List[str]]) -> List[Tuple[int, int]]:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        result = []
        i, j = coord
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                continue
            result.append((ni, nj))
        return result
    def shortestPath(self, grid: List[List[str]]) -> int:
        # Step 1: Find start coordinate
        start = (-1, -1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "*":
                    start = (i, j)
                    break

        # Step 2: BFS to find shortest path with visited set
        visited = set([start])
        q = deque([(start, 0)])
        while q:
            curr, path = q.popleft()
            for n in self.neighbours(curr, grid):
                ni, nj = n
                if n in visited or grid[ni][nj] == "X":
                    continue
                if grid[ni][nj] == "#":
                    return path + 1
                visited.add(n)
                q.append((n, path + 1))
        return -1

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
