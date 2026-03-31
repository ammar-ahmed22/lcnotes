## Intuition
Calculate the area for each island when it is seen and mark that island as visited.

## Implementation
We can iterate over each node in the grid and if it is a 1, we use DFS to calculate the area for that island and mark all those nodes as visited at the same time to avoid double counting.

For the DFS function, our base case is when the node is not a `1`, we return `0` as the area then. Otherwise, we mark that node as visited by setting it to `0` and start our count at 1. Then, we iterate over all the neighbours of the node (provided they are in bounds), and add the result for the recursive call to our count. Finally, we return the count.

## Complexity
- Time: `O(m * n)`, in the worst case, the whole grid is an island so we will DFS through the whole grid in the first iteration and then never again.
- Space: `O(m * n)`, recursive call stack.
