## Intuition
A tree is balanced if every node's left and right subtrees differ in height by at most 1. Compute heights recursively, using -1 as a sentinel to propagate imbalance upward.

## Implementation
Create a height function that returns -1 if imbalanced. Base case: None returns 0. Recursively get left and right heights. If either is -1, or their difference exceeds 1, return -1. Otherwise return 1 + max(left, right). The tree is balanced if the root's height is not -1.

## Edge-cases
The sentinel -1 allows early termination—once we find imbalance anywhere, we stop computing heights and propagate the failure upward.

## Complexity
Time `O(n)` visiting each node once. Space `O(h)` for the recursive call stack.
