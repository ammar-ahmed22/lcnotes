from typing import Optional
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(node: Optional[TreeNode], max_val: int):
            nonlocal good_nodes
            if not node:
                return
            if max_val <= node.val:
                good_nodes += 1
            dfs(node.right, max(max_val, node.val))
            dfs(node.left, max(max_val, node.val))

        dfs(root, root.val)
        return good_nodes
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
