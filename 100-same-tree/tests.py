import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("p, q, expected", [
    (TreeNode.create(1, 2, 3), TreeNode.create(1, 2, 3), True),
    (TreeNode.create(1, 2), TreeNode.create(1, None, 2), False),
    (TreeNode.create(1, 2, 1), TreeNode.create(1, 1, 2), False),
])
def test_same_tree(p, q, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.isSameTree(p, q) == expected
