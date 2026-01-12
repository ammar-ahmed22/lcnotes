import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, p, q, expected", [
    (TreeNode.create(6,2,8,0,4,7,9,None,None,3,5), TreeNode.create(2), TreeNode.create(8), TreeNode.create(6)),
    (TreeNode.create(6,2,8,0,4,7,9,None,None,3,5), TreeNode.create(2), TreeNode.create(4), TreeNode.create(2)),
    (TreeNode.create(2, 1), TreeNode.create(2), TreeNode.create(1), TreeNode.create(2)),
])
def test_lowest_common_ancestor_of_a_binary_search_tree(root, p, q, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.lowestCommonAncestor(root, p, q).val == expected.val
