import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0, 0, 0]])
])
def test_3sum(nums, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    result = solution.threeSum(nums)
    for triplet in result:
        triplet.sort()
    result.sort()

    for triplet in expected:
        triplet.sort()
    expected.sort()

    assert result == expected
