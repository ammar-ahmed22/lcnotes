import pytest
from solution import Solution

@pytest.mark.parametrize("candidates, target, expected", [
    ([2,3,6,7], 7, [[2,2,3],[7]]),
    ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ([2], 1, []),
])
def test_combination_sum(candidates, target, expected):
    solution = Solution()
    assert sorted(solution.combinationSum(candidates, target)) == sorted(expected)
