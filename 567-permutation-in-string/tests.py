import pytest
from solution import Solution

@pytest.mark.parametrize("s1, s2, expected", [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
])
def test_permutation_in_string(s1, s2, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.checkInclusion(s1, s2) == expected
