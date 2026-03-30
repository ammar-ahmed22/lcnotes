import pytest
from solution import Solution

@pytest.mark.parametrize("grid, expected", [
   ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1),
    ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 3),
])
def test_number_of_islands(grid, expected):
    solution = Solution()
    assert solution.numIslands(grid) == expected
