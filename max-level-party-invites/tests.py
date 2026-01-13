import pytest
from solution import Solution

@pytest.mark.parametrize("levels, reporting_chain, expected", [
    ([10, 9, 9, 5, 5, 5, 6], [[0, 1], [0,2], [1, 3], [1, 4], [1, 5], [2, 6]], 31),
    ([8, 6, 7, 4, 5], [[0, 1], [1, 2], [2, 3], [3, 4]], 20),
    ([10, 9], [[0, 1]], 10),
])
def test_max_level_party_invites(levels, reporting_chain, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.maxLevelPartyInvites(levels, reporting_chain) == expected
