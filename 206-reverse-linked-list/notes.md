## Intuition
To reverse a linked list in place, we need to reverse each node's next pointer to point to its previous node instead of its next node.

## Implementation
Maintain two pointers: `curr` (starting at head) and `prev` (starting at None). For each node, save its next pointer, reverse it to point to prev, then advance both pointers. When curr becomes None, prev points to the new head.

## Edge-cases
The order of operations matters: save next before overwriting it, then update the link, then move pointers. An empty list (head is None) works correctly since the loop never executes.

## Complexity
Time `O(n)` for a single pass through the list. Space `O(1)` using only pointers.
