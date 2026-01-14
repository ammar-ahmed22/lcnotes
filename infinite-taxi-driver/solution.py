from typing import List, Tuple
from collections import deque

class Solution:
    def neighbours(self, coord: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        dirs = [("N", (0, 1)), ("S", (0, -1)), ("W", (-1, 0)), ("E", (1, 0))]
        result = []
        x, y = coord
        for cardinal, dir in dirs:
            dx, dy = dir
            nx, ny = x + dx, y + dy 
            result.append((cardinal, (nx, ny)))
        return result
    
    def manhattan(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def findPath(self, cab: Tuple[int, int], destination: Tuple[int, int], barriers: List[Tuple[int,int]]) -> str:
        if cab == destination:
            return ""

        q = deque([(cab, "")])
        visited = set([cab])
        blocked = set(barriers)
        while q:
            curr, path = q.popleft()
            for n_dir, n_coord in self.neighbours(curr):
                if n_coord in visited or n_coord in blocked:
                    continue
                if n_coord == destination:
                    return path + n_dir
                
                q.append((n_coord, path + n_dir))
                visited.add(n_coord)
        return ""

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
