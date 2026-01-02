from typing import Optional
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            lh = height(root.left)
            if lh == -1:
                return -1
            
            rh = height(root.right)
            if rh == -1:
                return -1
            
            if abs(lh - rh) > 1:
                return -1
            
            return 1 + max(lh, rh)

        return height(root) != -1
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
