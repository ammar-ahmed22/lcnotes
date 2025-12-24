from typing import Optional
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        return max(self.dfs(root.left, depth + 1), self.dfs(root.right, depth + 1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
