import pytest
from solution import Solution

@pytest.mark.parametrize("start, target, blocked, expected", [
    ("0000", "0202", ["0201","0101","0102","1212","2002"], 6),
    ("1234", "1236", [], 2),
    ("5555", "5559", ["5556", "5557", "5558"], 6),
])
def test_minimum_lock_turns(start, target, blocked, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.minLockTurns(start, target, blocked) == expected
