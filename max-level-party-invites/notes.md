## Intuition
This is a tree DP problem similar to House Robber III. For each node, we track two states: the maximum sum if we invite this node (must skip children) versus if we skip this node (can choose either for children).

## Implementation
Build an adjacency list from the reporting chain and identify root nodes (those without parents). DFS from each root computing two values per node: `invite` (node's level + sum of children's skip values) and `skip` (sum of max(invite, skip) for each child). Memoize results to avoid recomputation.

## Edge-cases
The graph may have multiple disconnected trees (multiple roots). Process each root separately and sum their contributions.

## Complexity
Time `O(n)` with memoization ensuring each node is processed once. Space `O(n)` for the adjacency list and memoization map.
