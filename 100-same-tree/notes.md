## Intuition
Two trees are the same if their structures are identical and corresponding nodes have equal values. Recursively compare nodes in parallel.

## Implementation
Base case: if both nodes are None, they're equal. If exactly one is None or their values differ, they're not equal. Otherwise, recursively check that both left subtrees are the same AND both right subtrees are the same.

## Edge-cases
The comparison handles all combinations: both None (equal), one None (not equal), both present (compare values and recurse).

## Complexity
Time `O(n)` visiting each node. Space `O(h)` for the recursive call stack, where h is the tree height.
