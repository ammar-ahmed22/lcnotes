import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(3,2,3,None,3,None,1), 7),
    (TreeNode.create(3,4,5,1,3,None,1), 9),
])
def test_house_robber_iii(root, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.rob(root) == expected
