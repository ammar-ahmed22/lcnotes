from typing import List, Tuple

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def neighbs(i: int, j: int) -> List[Tuple[int, int]]:
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            res = []
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= len(grid) or nj < 0 or nj >= m:
                    continue
                res.append((ni, nj))
            return res


        def consume(i: int, j: int):
            if grid[i][j] != "1":
                return
            grid[i][j] = "0"
            for ni, nj in neighbs(i, j):
                consume(ni, nj)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    consume(i, j)

        return count



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
