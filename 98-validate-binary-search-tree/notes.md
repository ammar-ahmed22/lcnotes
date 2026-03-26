## Intuition
A node is valid when it is in the range of values that is decided by it's ancestors. When going deeper, the range is updated. For the root, the range starts with `(-inf, inf)`, going left upper bound is updated, going right lower bound is updated.

## Implementation
This problem can be solved with DFS. We start by defining our recursive function that takes in a node and the left and right bounds. If the node is `None`, that is valid node, we can return `True`. Otherwise, we check if the value is NOT in the range and early return false. Finally, we call the function recursively on left AND right with the updates bounds. For the left node, the lower bound stays the same but the upper bound is updated to the current value. For the right node, the lower bound is updated to the current value and the upper bound stays the same.

Finally, we call the recursive function on the root with `-inf, inf` as our bounds (using `sys.maxsize` or `float("inf")`/`float("-inf')`).

## Complexity
- Time: `O(n)`, we visit each node, at most, once.
- Space: `O(n)`, recursive call stack
