## Intuition
Interweave new nodes into the original list so that the next pointer of the old list points to the corresponding new node, making assigning random pointers trivial by the next node.

## Implementation
Start by interveaving the new nodes into the original list (i.e. `old1 -> new1 -> old2 -> new2 -> etc.`). Iterate over the original list, save the next node in a temporary variable (`next`), set `curr.next` to the new node with the current value and next pointing to `next`, set `curr = next`. 

After the interweaving is complete, we want to iterate again and assign the random pointers. Iterate starting from head while `curr and curr.next`. If `curr` (old) has a random pointer (not null), set `curr.next.random` (new node's random) to `curr.random.next` (old node's random -> next, which is the new node).

After the random pointers are assigned, we simply need to construct the resultant list by starting from `head.next` (first new node) and skipping over each next node(old node). The resultant list will be stored in `head.next`.

## Complexity
- Time: `O(n)` - iterate over the original list 3 times, sequentially (interweaving, random pointers, result)
- Space: `O(1)` - no extra space created
