import pytest
from solution import Solution

@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
])
def test_valid_palindrome(s, expected):
    # Write your test assertions here
    solution = Solution()
    assert solution.isPalindrome(s) == expected
