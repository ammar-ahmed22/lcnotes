from typing import Optional
from lcutils import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Find the mid-point (slow and fast) O(n)
        slow = head
        fast = head.next if head else None
        while fast and fast.next:
            slow = slow.next if slow else None
            fast = fast.next.next

        # Step 2: Reverse the second half O(n)
        second: Optional[ListNode] = None
        prev: Optional[ListNode] = None
        if slow:
            second = slow.next
            slow.next = None # break the link in the original list
            while second:
                temp = second.next
                second.next = prev
                prev = second
                second = temp

        # Step 3: Merge the two lists O(n)
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2




if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
