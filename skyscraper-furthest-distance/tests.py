import pytest
from solution import Solution

@pytest.mark.parametrize("heights, springs, sandbags, expected", [
    ([2, 3, 5, 1, 7], 1, 2, 3),
    ([4, 2, 2, 6, 3, 7], 1, 4, 5),
    ([1, 5, 2, 3, 10], 1, 3, 3),
])
def test_skyscraper_furthest_distance(heights, springs, sandbags, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.furthestDistance(heights, springs, sandbags) == expected
