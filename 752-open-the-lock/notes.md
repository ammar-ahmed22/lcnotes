## Intuition
Model this as a graph problem where each lock combination is a node and each wheel turn is an edge. Each state has exactly 8 neighbors (4 wheels × 2 directions). BFS finds the shortest path from "0000" to the target.

## Implementation
Create a function to generate all 8 neighbors of a combination (turn each wheel up or down using mod 10). Start BFS from "0000" with a queue storing (combo, turns) pairs. Track visited states to avoid cycles. For each state, check neighbors—skip if visited or a deadend. If a neighbor equals the target, return `turns + 1`.

## Edge-cases
Check if "0000" is a deadend (return -1 immediately). Also handle the case where the target is "0000" (return 0).

## Complexity
- Time: `O(10⁴)` — at most 10,000 possible states
- Space: `O(10⁴)` — visited set and queue
