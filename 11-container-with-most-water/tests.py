import pytest
from solution import Solution

@pytest.mark.parametrize("height, expected", [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
])
def test_container_with_most_water(height, expected):
    # Write your test assertions here
    solution = Solution()
    assert solution.maxArea(height) == expected
