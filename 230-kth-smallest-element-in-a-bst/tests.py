import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, k, expected", [
    (TreeNode.create(3,1,4,None,2), 1, 1),
    (TreeNode.create(5,3,6,2,4,None,None,1), 3, 3),
])
def test_kth_smallest_element_in_a_bst(root, k, expected):
    solution = Solution()
    assert solution.kthSmallest(root, k) == expected
