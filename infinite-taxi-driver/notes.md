## Intuition
On an infinite grid with barriers, BFS finds the shortest path. Each cell has 4 neighbors (N, S, E, W), and we track the path as a string of directions.

## Implementation
Generate neighbors as (direction, coordinate) pairs. No bounds checking needed on an infinite grid. BFS from start with queue entries of (coordinate, path_string). Track visited coordinates. For each neighbor, skip if visited or a barrier. If it's the destination, return the accumulated path. Otherwise, add to queue with the extended path.

## Edge-cases
If start equals destination, return empty string. The algorithm guarantees the shortest path due to BFS properties. Could be optimized with A* using Manhattan distance heuristic.

## Complexity
- Time: `O(V)` — where V is the number of reachable states
- Space: `O(V)` — visited set and queue
