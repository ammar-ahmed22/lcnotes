import pytest
from solution import Solution

@pytest.mark.parametrize("temperatures, expected", [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0])
])
def test_daily_temperatures(temperatures, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.dailyTemperatures(temperatures) == expected
