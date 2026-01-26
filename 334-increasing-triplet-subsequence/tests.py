import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4,5], True),
    ([5, 4, 3, 2, 1], False),
    ([2,1,5,0,4,6], True),
])
def test_increasing_triplet_subsequence(nums, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
