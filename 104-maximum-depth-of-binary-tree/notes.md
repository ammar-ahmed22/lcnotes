## Intuition
The maximum depth is the longest path from root to any leaf. Recursively, it's 1 plus the maximum of the left and right subtree depths.

## Implementation
Use DFS with a recursive function that returns the depth. Base case: if the node is None, return the current depth (0 if counting edges, or the accumulated depth if passing it down). Otherwise, return the maximum of recursing on left and right children with incremented depth.

## Edge-cases
An empty tree (root is None) has depth 0.

## Complexity
Time `O(n)` visiting every node. Space `O(h)` where h is the tree height, due to the recursive call stack. In the worst case (skewed tree), this is O(n).
