import pytest
from solution import Solution

@pytest.mark.parametrize("strs, expected", [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]]),
])
def test_group_anagrams(strs, expected):
    # Write your test assertions here
    solution = Solution()
    result = solution.groupAnagrams(strs)
    for arr in result:
        arr.sort()
    result.sort()

    for arr in expected:
        arr.sort()
    expected.sort()

    assert result == expected
