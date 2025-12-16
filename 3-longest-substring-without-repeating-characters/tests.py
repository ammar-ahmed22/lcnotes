import pytest
from solution import Solution

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
])
def test_longest_substring_without_repeating_characters(s, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected
