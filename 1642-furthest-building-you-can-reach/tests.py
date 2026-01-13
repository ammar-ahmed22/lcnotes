import pytest
from solution import Solution

@pytest.mark.parametrize("heights, bricks, ladders, expected", [
    ([4,2,7,6,9,14,12], 5, 1, 4),
    ([4,12,2,7,3,18,20,3,19], 10, 2, 7),
    ([14,3,19,3], 17, 0, 3),
])
def test_furthest_building_you_can_reach(heights, bricks, ladders, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.furthestBuilding(heights, bricks, ladders) == expected
