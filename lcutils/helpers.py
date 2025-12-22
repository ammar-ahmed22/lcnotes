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

def list_to_str(head: Optional[ListNode]) -> str:
    s = ""
    curr = head
    while curr:
        s += f"{curr.val} -> "
        curr = curr.next
    s += "None"
    return s
