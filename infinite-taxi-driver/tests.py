import pytest
from solution import Solution

@pytest.mark.parametrize("cab, destination, barriers, expected", [
    # Add test cases here as a tuple of (parameter1, parameter2, expected)
    # Adjust for the number of parameters you have
    # e.g. for twoSum, ([1, 2, 3, 4], 3, [0, 1])
    ((3, 0), (8, 3), [(7,0), (7,1), (7, 2), (7,3), (7,4), (8,2)], "NNNNNEEEEESS")
])
def test_infinite_taxi_driver(cab, destination, barriers, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert len(solution.findPath(cab, destination, barriers)) == len(expected)
