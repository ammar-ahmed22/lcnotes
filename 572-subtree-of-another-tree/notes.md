## Intuition
A subtree must match exactly starting from some node in the main tree. We need to check at every node whether the subtree rooted there is identical to subRoot.

## Implementation
Create a helper function `isSame` that checks if two trees are identical (same structure and values). In the main function, if subRoot is null, it's trivially a subtree. If root is null but subRoot isn't, return false. Check if the current root matches subRoot using `isSame`. If not, recursively check if subRoot is a subtree of either the left or right child.

## Edge-cases
A null subRoot is considered a subtree of any tree. Handle the case where root becomes null during recursion (subRoot can't exist in an empty tree).

## Complexity
- Time: `O(m * n)` — where m and n are the sizes of the two trees
- Space: `O(n)` — recursion stack
