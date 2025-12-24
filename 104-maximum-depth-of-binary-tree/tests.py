import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(3,9,20,None,None,15,7), 3),
    (TreeNode.create(1, None, 2), 2)
])
def test_maximum_depth_of_binary_tree(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.maxDepth(root) == expected
