from typing import List, Optional


class ListNode:
    @classmethod
    def from_arr(cls, nums: List[int]) -> Optional["ListNode"]:
        if len(nums) == 0:
            return None
        head = cls(nums[0])
        curr = head
        for i in range(1, len(nums)):
            curr.next = cls(nums[i])
            curr = curr.next
        return head

    @classmethod
    def create(cls, *nums: int) -> Optional["ListNode"]:
        return cls.from_arr(list(nums))
    
    @staticmethod
    def add_cycle(head: Optional["ListNode"], pos: int):
        if pos < 0 or not head:
            return head
        curr = head
        point_to = None
        i = 0
        while curr:
            if i == pos:
                point_to = curr
            if not curr.next:
                break
            curr = curr.next
            i += 1
        if point_to:
            curr.next = point_to
        return head

    def __str__(self) -> str:
        s = ""
        curr = self
        while curr:
            s += f"{curr.val} -> "
            curr = curr.next
        s += "None"
        return s

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
