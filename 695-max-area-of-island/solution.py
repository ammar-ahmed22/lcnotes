from typing import List, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def neighbs(i: int, j: int) -> List[Tuple[int, int]]:
            res = []
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                res.append((ni, nj))

            return res

        def dfs(i: int, j: int) -> int:
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            curr = 1
            for ni, nj in neighbs(i, j):
                curr += dfs(ni, nj)
            return curr

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
