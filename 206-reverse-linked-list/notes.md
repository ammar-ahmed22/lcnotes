## Intuition
To reverse a linked list, we need to flip each node's pointer to point backward instead of forward. This can be done iteratively by maintaining references to the previous and current nodes.

## Implementation
Use two pointers: `curr` starting at `head` and `prev` starting at `None`. For each node, save `curr.next` in a temp variable (we'll lose access to it otherwise), then reverse the link by setting `curr.next = prev`. Advance by setting `prev = curr` and `curr = temp`. When done, `prev` points to the new head.

## Edge-cases
The order of operations is critical. Always save the next pointer before overwriting it. An empty list or single-node list works naturally—`prev` will be `None` or the single node respectively.

## Complexity
- Time: `O(n)` — visit each node once
- Space: `O(1)` — only using pointers
