## Intuition
Level order traversal of binary tree is done with queue, but we need to process all the same level together.

## Implementation
Basic level order traversal where we simply want to print the values or do something with each level sequentially is quite simple with a queue, just dequeue process and then push the right and left if they exist. However, in this problem, we want to add all values from a given level to an array and then add that array to the result, therefore, we can't simply store the nodes by individually in the queue. Each queue element should contain all nodes for that level.

The queue will consist of an array of nodes for that level. Start off by initializing the queue with its first element being an array containing just the root (level1). Then, iterate while the queue is not empty, dequeue the nodes from the queue. Initialize a temporary array for the values that will be pushed to the result and another array for the level nodes that will be pushed to the queue after processing the current nodes. Iterate over the nodes, add the value to the temporary array. If the node has left, add that node to the level nodes array, same with right. After this iteration, we add the temporary array to the result and check if the level nodes are not empty and add them to the queue.

## Edge-cases
If the root is null, return empty array early.

## Complexity
- Time: `O(n)`: we process each node once.
- Space: `O(n)`: the queue can contain all the nodes at worst
