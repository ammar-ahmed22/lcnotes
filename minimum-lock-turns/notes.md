## Intuition
Each lock combination is a graph node with 8 neighbors (4 wheels × 2 directions). BFS from start to target finds the minimum number of turns, avoiding blocked combinations.

## Implementation
Generate neighbors by turning each wheel up or down (using mod 10 for wraparound). Start BFS with (start_combo, 0) in the queue and a visited set. For each state, try all neighbors—skip if visited or blocked. If a neighbor is the target, return `turns + 1`. Otherwise, add to queue and visited.

## Edge-cases
Check if start equals target (return 0) or if start is blocked (return -1) before starting BFS.

## Complexity
- Time: `O(10⁴)` — at most 10,000 possible states
- Space: `O(10⁴)` — visited set and queue
