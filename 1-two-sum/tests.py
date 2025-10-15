import pytest
from solution import Solution

@pytest.mark.parametrize("nums, target, expected", [
    # Add test cases here as a tuple of (parameter1, parameter2, expected)
    # Adjust for the number of parameters you have
    # e.g. for twoSum, ([1, 2, 3, 4], 3, [0, 1])
])
def test_two_sum(nums, target, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()