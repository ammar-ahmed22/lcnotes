from typing import Optional
from lcutils import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        while n > 0:
            right = right.next if right else None
            n -= 1

        dummy = ListNode()
        dummy.next = head
        left = dummy
        while left and right:
            left = left.next
            right = right.next

        if left and left.next:
            left.next = left.next.next
        return dummy.next
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
