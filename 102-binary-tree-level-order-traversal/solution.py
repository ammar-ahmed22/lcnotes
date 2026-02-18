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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        q = deque([[root]])
        while q:
            nodes = q.popleft()
            temp = []
            level_nodes = []
            for node in nodes:
                temp.append(node.val)
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            if level_nodes:
                q.append(level_nodes)
            result.append(temp)

        return result


if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
    root = TreeNode.create(1,2,3,4,None,None,5)
    print(str(root))
    
