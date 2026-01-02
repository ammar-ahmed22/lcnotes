import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(3,9,20,None,None,15,7), True),
    (TreeNode.create(1,2,2,3,3,None,None,4,4), False),
    (None, True)
])
def test_balanced_binary_tree(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.isBalanced(root) == expected
