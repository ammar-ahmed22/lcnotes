from typing import Optional
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = root.val if root else 0
        def dfs(node: Optional[TreeNode]):
            nonlocal count, res
            if not node:
                return
            
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res


if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
