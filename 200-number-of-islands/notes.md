## Intuition
Whenever we see an island, we should mark the whole island as visited.

## Implementation
We can solve this by iterating over the entire grid and whenever we see an island (`1`), we mark the whole island as visited with DFS and flipping the node to `0`.

We start by iterating over the whole grid:
- On each iteration, if the node is `1`, we call a recursive function `consume(i, j)` that will use DFS to mark the whole island as visited.
- We also increment our global count here.

For the `consume(i, j)` function:
- If the node at `i,j` is not `1`, we return early
- Otherwise, we mark that node as visited by flipping it to `0`
- Next, we iterate over all 4 (at most 4, can be less if at edge) neighbours of `i,j` and call the function recursively

This means that after the `consume` function is called on a `1` in the main iteration, the whole island will be marked as `0` and we can continue iterating.

## Edge-cases
The neighbours should be checked to ensure they are in bounds correctly.

## Complexity
- Time: `O(m * n)`, we iterate over the entire grid once and recursively mark each island as visited. In the worst-case, the whole grid is an island so we will only go over all nodes once in the recursive function.
- Space: `O(m * n)`, for the recursive call stack
