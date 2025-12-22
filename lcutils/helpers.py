from typing import List, Optional
from .structures import ListNode

def arr_to_list(arr: List[int]) -> Optional[ListNode]:
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def to_list(*nums: int) -> Optional[ListNode]:
    return arr_to_list(list(nums))

def add_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
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

def list_to_str(head: Optional[ListNode]) -> str:
    s = ""
    curr = head
    while curr:
        s += f"{curr.val} -> "
        curr = curr.next
    s += "None"
    return s
