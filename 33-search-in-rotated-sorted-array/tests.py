import pytest
from solution import Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1)
])
def test_search_in_rotated_sorted_array(nums, target, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.search(nums, target) == expected
