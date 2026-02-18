from typing import List, Optional
from lcutils import ListNode
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        ptrs: List[Optional[ListNode]] = [None] * k
        heap = []
        for i in range(k):
            ptr = lists[i]
            ptrs[i] = ptr
            if ptr:
                heapq.heappush(heap, (ptr.val, i))
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            # will be defined because it was added
            ptrs[i] = ptrs[i].next
            if ptrs[i]:
                heapq.heappush(heap, (ptrs[i].val, i))
        return dummy.next



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()

