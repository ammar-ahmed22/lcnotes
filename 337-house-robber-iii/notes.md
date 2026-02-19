## Intuition
We want to calculate the max amount the robber can take if they decide to steal from each house or to skip that house. Stealing would necessitate skipping over the direct children, and in the case of skipping we don't care whether we skip or take the child, we just want the max.

## Implementation
In order to process nodes only once, we'll initialize a hashmap for the node stored with its take and skip value. Define the recursive DFS function, the base case checks if the node exists in the hashmap and early returns. Otherwise, we initialize a take value and skip value for the current node. The take value is initialized to the node's value and the skip value is initialized to zero. Then we iterate over each of the children and call the function recursively for each child. We add the skip value for the child to the take value for the current node to represent that the child is skipped when we decide to take the node. For the skip value of the current node we add the max of the take and skip value for the child because we don't care whether we skip the child or take it, we just want the max.

After iterating over the children, we save the node and the take and skip values in the hashmap to ensure processing only once and return them.

Finally, we call the function on the root node and take the max of the values.

## Complexity
- Time: `O(n)`, we iterate through each node once.
- Space: `O(n)`, the hashmap will contain all of the nodes as well as the call stack
