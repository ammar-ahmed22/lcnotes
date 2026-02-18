import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(3,9,20,None,None,15,7), [[3], [9, 20], [15, 7]]),
    (TreeNode.create(1), [[1]]),
    (None, []),
    (TreeNode.create(1,2,3,4,None,None,5), [[1],[2,3],[4,5]])
])
def test_binary_tree_level_order_traversal(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    result = solution.levelOrder(root)
    assert result == expected
