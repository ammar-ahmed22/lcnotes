## Intuition
A tree is balanced if the depth difference between left and right subtrees never exceeds 1 at any node. We can combine the balance check with height calculation by using a sentinel value (`-1`) to propagate imbalance upward.

## Implementation
Use a recursive DFS function that returns the height of a subtree, or `-1` if it's unbalanced. Base case: null node returns `0`. Recurse on the left subtree—if it returns `-1`, immediately propagate `-1` upward. Do the same for the right subtree. If both subtrees are balanced, check if their height difference exceeds 1; if so, return `-1`. Otherwise, return `1 + max(left, right)`. In the main function, the tree is balanced if DFS doesn't return `-1`.

## Edge-cases
An empty tree is considered balanced (returns height 0).

## Complexity
- Time: `O(n)` — visit each node once
- Space: `O(h)` — recursion stack depth equals tree height
