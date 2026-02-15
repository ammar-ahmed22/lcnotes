## Intuition
Since both lists are sorted, the smallest element is always at one of the two heads. Compare them, take the smaller one, and advance that list's pointer.

## Implementation
Create a dummy node to simplify edge cases. Use a curr pointer starting at dummy. While both lists have nodes, compare their values, append the smaller one to curr, and advance the appropriate pointer. After one list is exhausted, append the remainder of the other list.

## Edge-cases
Using a dummy node eliminates special handling for the result's head. One or both input lists might be empty, which the algorithm handles naturally.

## Complexity
Time `O(m + n)` visiting each node once. Space `O(1)` if we reuse existing nodes, or `O(m + n)` if creating new nodes.
