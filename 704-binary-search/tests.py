import pytest
from solution import Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1),
])
def test_binary_search(nums, target, expected):
    # Write your test assertions here
    solution = Solution()
    assert solution.search(nums, target) == expected
