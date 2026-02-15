## Intuition
Since both lists are sorted, we can build the merged list by always taking the smaller of the two current nodes. This is similar to the merge step in merge sort.

## Implementation
Create a dummy node to simplify head handling and a `curr` pointer for building the result. While both lists have nodes, compare their values—append the smaller one to the result and advance that list's pointer. After the main loop, one list may have remaining nodes; append them directly since they're already sorted.

## Edge-cases
If either list is initially empty, the other list is returned as-is. The dummy node eliminates special case handling for the first element.

## Complexity
- Time: `O(m + n)` — each node visited once
- Space: `O(1)` — reusing existing nodes (or `O(m + n)` if creating new nodes)
