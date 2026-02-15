## Intuition
Inverting a binary tree means swapping every node's left and right children. We can visit every node using either BFS or DFS and perform the swap.

## Implementation
Using BFS: initialize a queue with the root. For each node dequeued, swap its left and right children, then enqueue both children if they exist. Continue until the queue is empty. Return the original root reference.

## Edge-cases
If the root is None, return None immediately—there's nothing to invert.

## Complexity
Time `O(n)` visiting every node once. Space `O(n)` for the queue, which at worst holds an entire level of the tree.
