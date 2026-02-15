## Intuition
On an infinite grid with obstacles, BFS finds the shortest path while building a direction string. Each move adds its cardinal direction (N, S, E, W) to the path.

## Implementation
BFS from start, tracking both the coordinate and the path string. Generate 4 neighbors (N, S, E, W) for each position. Skip barriers and visited cells. When reaching the target, return the accumulated direction string.

## Edge-cases
No bounds checking needed since the grid is infinite. If start equals target, return an empty string.

## Complexity
Time and Space `O(d^2)` where d is the distance to target, since BFS explores in expanding circles. Could be optimized with A* using Manhattan distance heuristic.
