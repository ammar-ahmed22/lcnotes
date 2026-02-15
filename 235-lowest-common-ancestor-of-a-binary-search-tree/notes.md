## Intuition
In a BST, the LCA is the first node where p and q diverge—one goes left, the other goes right (or one equals the current node). This is the split point in the BST ordering.

## Implementation
Start at the root. If both p and q are greater than current, move right. If both are less, move left. Otherwise, current is the LCA—either it's a split point, or one of p/q equals current.

## Edge-cases
The problem guarantees valid inputs with p and q existing in the tree, so no null checks needed beyond the traversal.

## Complexity
Time `O(h)` where h is the tree height. Space `O(1)` using iterative traversal.
