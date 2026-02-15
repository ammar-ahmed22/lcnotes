## Intuition
This is a standard BFS shortest path problem on a grid. Start from the initial position and explore all reachable cells level by level until finding food.

## Implementation
Locate the start cell (marked with '*'). BFS from there: for each cell, check all four neighbors. Skip visited cells and obstacles ('X'). When reaching a food cell ('#'), return the path length. Mark cells as visited when adding to the queue.

## Edge-cases
If no path to food exists (all food is blocked or unreachable), return -1 after BFS completes.

## Complexity
Time `O(m * n)` visiting each cell at most once. Space `O(m * n)` for the visited set and queue.
