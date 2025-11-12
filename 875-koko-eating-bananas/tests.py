import pytest
from solution import Solution

@pytest.mark.parametrize("piles, h, expected", [
    ([3,6,7,11], 8, 4),
    ([30,11,23,4,20], 5, 30),
    ([30,11,23,4,20], 6, 23)
])
def test_koko_eating_bananas(piles, h, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.minEatingSpeed(piles, h) == expected
