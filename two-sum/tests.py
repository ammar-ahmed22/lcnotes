import pytest
from solution import Solution

@pytest.mark.parametrize("nums, target, expected", [
    # Add test cases here as a tuple of (parameter1, parameter2, expected)
    # Adjust for the number of parameters you have
    # e.g. for twoSum, ([1, 2, 3, 4], 3, [0, 1])
    ([2,7,11,15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_two_sum(nums, target, expected):
    solution = Solution()
    assert sorted(solution.twoSum(nums, target)) == sorted(expected)
