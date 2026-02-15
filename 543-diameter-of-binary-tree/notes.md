## Intuition
The diameter passes through some node where it equals the sum of the left subtree height plus the right subtree height. We need to check this sum at every node while computing heights.

## Implementation
Use DFS to compute heights while tracking the maximum diameter found. For each node, compute left and right subtree heights recursively. Update the global maximum with left_height + right_height. Return 1 + max(left, right) as this node's height contribution.

## Edge-cases
In Python, use the `nonlocal` keyword to modify a variable from an enclosing scope within the nested DFS function.

## Complexity
Time `O(n)` visiting every node once. Space `O(h)` for the call stack, which is O(n) in the worst case.
