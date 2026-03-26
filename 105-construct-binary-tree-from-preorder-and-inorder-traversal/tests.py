import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("preorder, inorder, expected", [
    ([3,9,20,15,7], [9,3,15,20,7], TreeNode.create(3,9,20,None,None,15,7)),
    ([-1], [-1], TreeNode.create(-1)),
])
def test_construct_binary_tree_from_preorder_and_inorder_traversal(preorder, inorder, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert str(solution.buildTree(preorder, inorder)) == str(expected)
