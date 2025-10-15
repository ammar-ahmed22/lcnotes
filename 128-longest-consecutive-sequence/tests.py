import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([1,0,1,2], 3),
])
def test_longest_consecutive_sequence(nums, expected):
    # Write your test assertions here
    solution = Solution()
    assert solution.longestConsecutive(nums) == expected
