import pytest
from solution import Solution

@pytest.mark.parametrize("candidates, target, expected", [
    ([10,1,2,7,6,1,5], 8, [[1,7],[1,1,6],[1,2,5],[2,6]]),
    ([2,5,2,1,2], 5, [[1,2,2],[5]]),
])
def test_combination_sum_ii(candidates, target, expected):
    solution = Solution()
    assert sorted(solution.combinationSum2(candidates, target)) == sorted(expected)
