## Intuition
Keep track of the largest node seen in the path.

## Implementation
Since we are going down the path, we use DFS. Define our recursive function to the node and a max value parameter. Base case is if the root is null, return. Otherwise, check if max value is less than or equal to the current node's value (i.e. the node is larger or equal to the largest value seen before this in its path), if true, increment the good nodes counter. Call the DFS function on left and right side taking the max of the current max value and the node's value.

## Complexity
- Time: `O(n)`, each node is processed once
- Space: `O(n)`, call stack
