import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(1, 2, 3, 4, 5), 3),
    (TreeNode.create(1, 2), 1),
])
def test_diameter_of_binary_tree(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.diameterOfBinaryTree(root) == expected
