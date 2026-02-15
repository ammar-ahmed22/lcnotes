## Intuition
The maximum depth of a binary tree is the longest path from root to any leaf. At each node, the depth is one plus the maximum depth of its subtrees.

## Implementation
Create a recursive DFS function that takes the current node and accumulated depth. When the node is `None`, we've gone past a leaf, so return the current depth. Otherwise, recurse on both children with `depth + 1` and return the maximum of the two results.

## Edge-cases
An empty tree (null root) returns 0, which the base case handles naturally.

## Complexity
- Time: `O(n)` — visit every node
- Space: `O(n)` — worst case recursion depth for a skewed tree; `O(log n)` for balanced
