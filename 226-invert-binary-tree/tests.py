from typing import Optional
import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(4, 2, 7, 1, 3, 6, 9), TreeNode.create(4,7,2,9,6,3,1)),
    (TreeNode.create(2,1,3), TreeNode.create(2,3,1)),
])
def test_invert_binary_tree(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    r = solution.invertTree(root)
    e: Optional[TreeNode] = expected
    assert [] if r is None else r.to_arr() == [] if e is None else e.to_arr()
