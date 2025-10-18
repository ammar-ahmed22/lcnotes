import pytest
from solution import Solution

@pytest.mark.parametrize("tokens, expected", [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    (["4","3","-"], 1)
])
def test_evaluate_reverse_polish_notation(tokens, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.evalRPN(tokens) == expected
