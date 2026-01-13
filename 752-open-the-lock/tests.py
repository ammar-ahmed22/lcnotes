import pytest
from solution import Solution

@pytest.mark.parametrize("deadends, target, expected", [
    (["0201","0101","0102","1212","2002"], "0202", 6),
    (["8888"], "0009", 1),
    (["8887","8889","8878","8898","8788","8988","7888","9888"], "8888", -1),
])
def test_open_the_lock(deadends, target, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.openLock(deadends, target) == expected
