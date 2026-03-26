import pytest
from solution import Solution
from lcutils import TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode.create(2, 1, 3), True),
    (TreeNode.create(5,1,4,None,None,3,6), False),
])
def test_validate_binary_search_tree(root, expected):
    solution = Solution()
    assert solution.isValidBST(root) == expected
