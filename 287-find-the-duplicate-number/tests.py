import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
    ([3,3,3,3,3], 3),
    ([2,5,9,6,9,3,8,9,7,1], 9)
])
def test_find_the_duplicate_number(nums, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.findDuplicate(nums) == expected
