from typing import List, Optional
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = { val: idx for idx, val in enumerate(inorder) }
        i = 0
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            nonlocal i
            if l > r:
                return None
            
            root_val = preorder[i]
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            i += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
