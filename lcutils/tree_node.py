from typing import List, Optional, Deque
from collections import deque


class TreeNode:
    @classmethod
    def from_arr(cls, arr: List[Optional[int]]) -> Optional["TreeNode"]:
        if not arr or arr[0] is None:
            return None
        
        nodes = [cls(v) if v is not None else None for v in arr]
        for i in range(len(nodes)):
            node = nodes[i]
            if node is None:
                continue
            li, ri = 2 * i + 1, 2 * i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]

        return nodes[0]
    
    @classmethod
    def create(cls, *nums: Optional[int]) -> Optional["TreeNode"]:
        return TreeNode.from_arr(list(nums))
    
    def to_arr(self) -> List[Optional[int]]:
        result = []
        q: Deque[Optional["TreeNode"]] = deque([self])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result


    def __init__(self, val=0, left: Optional["TreeNode"]=None, right: Optional["TreeNode"]=None):
        self.val = val
        self.left = left
        self.right = right
