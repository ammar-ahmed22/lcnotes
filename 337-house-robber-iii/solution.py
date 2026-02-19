from typing import Optional, Tuple
from lcutils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dp = {}
        def dfs(node: TreeNode) -> Tuple[int, int]:
            if node in dp:
                return dp[node]
            take_n = node.val
            skip_n = 0
            children = [node.left, node.right]
            for child in children:
                if not child:
                    continue
                take, skip = dfs(child)
                take_n += skip # if we decided to take the current node, direct children should be skipped
                skip_n += max(take, skip) # if we skip the current node, we don't care whether we take or skip the child, just want the max

            dp[node] = (take_n, skip_n)
            return dp[node]

        take, skip = dfs(root)
        return max(take, skip)



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
