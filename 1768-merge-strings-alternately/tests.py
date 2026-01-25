import pytest
from solution import Solution

@pytest.mark.parametrize("word1, word2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
])
def test_merge_strings_alternately(word1, word2, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.mergeAlternately(word1, word2) == expected
