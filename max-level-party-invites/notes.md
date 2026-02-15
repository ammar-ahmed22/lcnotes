## Intuition
This is a tree DP problem similar to "House Robber III." For each employee, we compute two values: the maximum sum if we invite them (must skip their direct reports) and if we skip them (can choose either for reports).

## Implementation
Build an adjacency list from the reporting chain and identify root employees (those without managers). DFS with memoization computes (invite, skip) pairs bottom-up. If we invite an employee, add their level plus the skip values of all reports. If we skip, add max(invite, skip) of each report. Process all roots and sum the maximum of invite/skip for each tree.

## Edge-cases
The graph may be a forest (multiple disconnected trees). Track which nodes have parents to identify all roots and process each independently.

## Complexity
- Time: `O(n)` — each node processed exactly once via memoization
- Space: `O(n)` — adjacency list and memoization cache
