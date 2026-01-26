import pytest
from solution import Solution

@pytest.mark.parametrize("chars, expected", [
    (["a","a","b","b","c","c","c"], ["a","2","b","2","c","3"]),
    (["a"], ["a"]),
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","1","2"]),
    (["a","a","a","b","b","a","a"], ["a","3","b","2","a","2"]),
])
def test_string_compression(chars, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.compress(chars) == len(expected)
    for i in range(len(expected)):
        assert chars[i] == expected[i]
