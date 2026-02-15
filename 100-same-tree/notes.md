## Intuition
Two trees are identical if their structure and node values match exactly. By traversing both trees simultaneously, we can compare nodes at each position.

## Implementation
Use recursive DFS to check both trees in parallel. The base case is when both `p` and `q` are null—this means we've reached the end of both subtrees successfully, so return true. If both nodes exist and their values match, recursively verify that the left subtrees are the same AND the right subtrees are the same. If any of these conditions fail, return false.

## Edge-cases
No special edge cases beyond the base conditions. The recursion naturally handles trees of different shapes or sizes since a mismatch (one null, one not) will return false.

## Complexity
- Time: `O(n)` — visit each node once
- Space: `O(h)` — recursion stack depth equals tree height
