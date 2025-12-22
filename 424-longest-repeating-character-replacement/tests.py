import pytest
from solution import Solution

@pytest.mark.parametrize("s, k, expected", [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
])
def test_longest_repeating_character_replacement(s, k, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.characterReplacement(s, k) == expected
