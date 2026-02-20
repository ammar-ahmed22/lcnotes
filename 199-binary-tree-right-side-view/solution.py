from typing import List, Optional
from lcutils import TreeNode
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([[root]])
        while q:
            nodes = q.popleft()
            result.append(nodes[0].val)
            level = []
            for node in nodes:
                if node.right:
                    level.append(node.right)
                if node.left:
                    level.append(node.left)
            if level:
                q.append(level)
        return result



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
