import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(3,1,4,3,None,1,5), 4),
    (TreeNode.create(3,3,None,4,2), 3),
    (TreeNode.create(1), 1)
])
def test_count_good_nodes_in_binary_tree(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.goodNodes(root) == expected
