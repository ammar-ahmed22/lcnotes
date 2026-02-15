## Intuition
The diameter passes through some node where the path goes down through its left and right subtrees. At each node, `left_height + right_height` is a candidate for the diameter. Track the maximum across all nodes.

## Implementation
Use DFS that returns the height of each subtree while updating a global result. Base case: null node returns 0. For each node, compute left and right heights recursively. Update the global maximum with `left + right` (the path through this node). Return `1 + max(left, right)` as this subtree's height.

## Edge-cases
In Python, use `nonlocal` to modify variables from an enclosing scope within a nested function. The diameter could be entirely within one subtree.

## Complexity
- Time: `O(n)` — visit each node once
- Space: `O(n)` — recursion stack depth in worst case
