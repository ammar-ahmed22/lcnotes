from typing import Optional
from lcutils import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2, curr = l1, l2, dummy
        carry = 0

        while p1 and p2:
            tot = p1.val + p2.val + carry
            val = tot
            carry = 0

            if tot >= 10:
                val = tot % 10
                carry = tot // 10
            
            curr.next = ListNode(val)
            curr = curr.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            tot = p1.val + carry
            val = tot
            carry = 0

            if tot >= 10:
                val = tot % 10
                carry = tot // 10
            
            curr.next = ListNode(val)
            curr = curr.next
            p1 = p1.next

        while p2:
            tot = p2.val + carry
            val = tot
            carry = 0
            if tot >= 10:
                val = tot % 10
                carry = tot // 10

            curr.next = ListNode(val)
            curr = curr.next
            p2 = p2.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
