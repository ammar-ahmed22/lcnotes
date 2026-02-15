## Intuition
By maintaining a gap of `n` nodes between two pointers, when the right pointer reaches the end, the left pointer will be just before the node to remove.

## Implementation
First, advance the right pointer `n` steps ahead. Create a dummy node pointing to the head to handle edge cases cleanly, and set the left pointer to the dummy. Move both pointers together until right reaches null. Now left is positioned just before the target node—skip over it by setting `left.next = left.next.next`.

## Edge-cases
The dummy node handles removing the first node (when n equals the list length). Without it, we'd need special case logic for updating the head.

## Complexity
- Time: `O(n)` — single pass through the list
- Space: `O(1)` — only using pointers
