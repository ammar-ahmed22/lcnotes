import pytest
from solution import Solution

@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
])
def test_valid_anagram(s, t, expected):
    # Write your test assertions here
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
