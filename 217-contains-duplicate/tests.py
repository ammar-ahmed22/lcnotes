import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
])
def test_contains_duplicate(nums, expected):
    # Write your test assertions here
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
