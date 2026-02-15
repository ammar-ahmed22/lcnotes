## Intuition
By maintaining two pointers n nodes apart, when the right pointer reaches the end, the left pointer is at the node just before the one to remove.

## Implementation
Advance the right pointer n positions. Create a dummy node pointing to head to handle edge cases. Position left at the dummy. Move both pointers together until right reaches None. Now left.next is the target node—skip it by setting left.next = left.next.next.

## Edge-cases
The dummy node handles removing the head node (when n equals list length). Without it, we'd need special logic for that case.

## Complexity
Time `O(n)` for a single pass. Space `O(1)` using only pointers.
