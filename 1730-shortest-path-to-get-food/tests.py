import pytest
from solution import Solution

@pytest.mark.parametrize("grid, expected", [
    ([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]], 3),
    ([["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]], -1),
    ([["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]], 6),
    ([["O","*"],["#","O"]], 2),
    ([["X","*"],["#","X"]], -1),
])
def test_1730_shortest_path_to_get_food(grid, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.shortestPath(grid) == expected
