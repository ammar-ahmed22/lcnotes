## Intuition
Finding the shortest path in an unweighted grid is a classic BFS problem. BFS explores all cells at distance k before any cell at distance k+1, guaranteeing the first food cell reached is the closest.

## Implementation
First, locate the starting position (`*`). Initialize a queue with the start coordinate and path length 0, plus a visited set. Process cells level by level: for each cell, check its four neighbors. Skip if visited or blocked (`X`). If it's food (`#`), return the current path length + 1. Otherwise, add to visited and queue with incremented path.

## Edge-cases
If BFS completes without finding food, return -1 (no reachable food). The visited set prevents revisiting cells and infinite loops.

## Complexity
- Time: `O(m * n)` — each cell visited at most once
- Space: `O(m * n)` — visited set and queue
