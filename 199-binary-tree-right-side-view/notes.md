## Intuition
Traverse levels and take the first element in the level ensuring we always add right side to each level first.

## Implementation
Essentially the same as level order traversal but we only want to grab the value from the first node on each level, ensuring to add the right side to the level first always.

Initialize result array and queue that starts with an array of just the root. Iterate while the queue is not empty. Pop the level nodes from the queue and add the value from the first node in the level to the result array (we will ensure that there is always at least one node in the level). Initialize a temporary array for the new level, iterate over the nodes in the current level, if the node has right, add to the new level array, if it has left add to the new level array (always in this order). After that iteration is complete, check if the new level is not empty and append to the queue. Return the result at the end.

## Edge-cases
Return early with empty array if root is None. 

Ensure that right side is added to the level first always.

## Complexity
- Time: `O(n)`, each node is processed once.
- Space: `O(n)`, the queue can contain all nodes
