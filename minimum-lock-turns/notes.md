## Intuition
Treat each combination as a node in a graph where edges connect combinations differing by one wheel turn. BFS finds the shortest path from start to target.

## Implementation
Create a neighbor function that generates all 8 possible combinations from one turn (each of 4 wheels can go up or down). BFS from start: for each combination, try all neighbors. Skip blocked or visited combinations. Return the number of turns when we reach the target.

## Edge-cases
If start equals target, return 0. If start is blocked, return -1 immediately since no moves are possible.

## Complexity
Time `O(10^4 * 8)` for BFS over all possible states, each with 8 neighbors. Space `O(10^4)` for visited set.
