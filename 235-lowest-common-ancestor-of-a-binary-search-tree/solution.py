from typing import Optional
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr:
            if q and p and q.val > curr.val and p.val > curr.val:
                curr = curr.right
            elif q and p and q.val < curr.val and p.val < curr.val:
                curr = curr.left
            else:
                return curr



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
