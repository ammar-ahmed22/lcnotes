import pytest
from solution import Solution

@pytest.mark.parametrize("n, expected", [
    (3, ["((()))","(()())","(())()","()(())","()()()"]),
    (1, ["()"]),
    (2, ["(())", "()()"])
])
def test_generate_parentheses(n, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert sorted(solution.generateParenthesis(n)) == sorted(expected)
