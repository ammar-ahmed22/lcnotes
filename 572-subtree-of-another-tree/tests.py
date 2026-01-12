import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, subRoot, expected", [
    (TreeNode.create(3, 4, 5, 1, 2), TreeNode.create(4, 1, 2), True),
    (TreeNode.create(3, 4, 5, 1, 2, None, None, None, None, 0), TreeNode.create(4, 1, 2), False),
])
def test_subtree_of_another_tree(root, subRoot, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == expected
