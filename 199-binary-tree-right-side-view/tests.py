import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(1,2,3,4,None,None,None,5), [1, 3, 4, 5]),
    (TreeNode.create(1,None,3), [1, 3]),
    (None, []),
])
def test_binary_tree_right_side_view(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.rightSideView(root) == expected
