import pytest
from solution import Solution

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1,2,1,2,1,2,3,1,3,2], 2, [1, 2]),
    ([3, 0, 1, 0], 1, [0])
])
def test_top_k_frequent_elements(nums, k, expected):
    # Write your test assertions here
    solution = Solution()
    assert sorted(solution.topKFrequent(nums, k)) == sorted(expected)
