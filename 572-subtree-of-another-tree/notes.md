## Intuition
Check if subRoot matches the tree rooted at any node of root. Use the "same tree" comparison at each node of root.

## Implementation
Create a helper function to check if two trees are identical (same structure and values). For the main function: if subRoot is None, it's trivially a subtree. If root is None but subRoot isn't, return False. Check if root matches subRoot using the helper. If not, recursively check the left and right subtrees of root.

## Edge-cases
A None subRoot is always a subtree. A None root with non-None subRoot is never a match.

## Complexity
Time `O(m * n)` in the worst case, comparing at each of n nodes with m-node comparison. Space `O(h)` for recursion depth.
