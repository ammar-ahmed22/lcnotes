## Intuition
In a BST, all nodes in the left subtree are smaller and all in the right are larger. The LCA is the first node where p and q diverge—one goes left, one goes right (or one equals the current node).

## Implementation
Solve iteratively for better space. Start at the root and traverse down. If both p and q are greater than the current value, move right. If both are smaller, move left. Otherwise, we've found the split point—this is the LCA.

## Edge-cases
The problem guarantees p and q exist in the tree, so we don't need null checks for them. One node being the ancestor of another is handled naturally—the divergence point will be that ancestor.

## Complexity
- Time: `O(h)` — traverse at most the height of the tree
- Space: `O(1)` — iterative approach uses no extra space
