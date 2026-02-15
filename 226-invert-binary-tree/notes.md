## Intuition
Inverting a tree means swapping every node's left and right children. We can traverse the tree using BFS (or DFS) and perform the swap at each node.

## Implementation
Handle the empty tree case first. Initialize a queue with the root. For each node dequeued, swap its left and right children. Then enqueue any non-null children to continue the traversal. Return the original root reference (now pointing to the inverted tree).

## Edge-cases
An empty tree (null root) should return null immediately. The algorithm handles single-node trees naturally.

## Complexity
- Time: `O(n)` — visit each node once
- Space: `O(n)` — queue holds up to n/2 nodes at the widest level
