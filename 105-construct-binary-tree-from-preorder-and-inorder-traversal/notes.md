## Intuition
The inorder traversal splits the tree into left and right at each node. In other words, everything to the right of the node in the inorder traversal is on the right side and everything on the left is on the left side.

## Implementation
We can use DFS to construct the tree in a pre-order fashion.

In our DFS function, we take in a range of left and right as parameters.
- If the left is greater than the right, we return None.
- We take the next value from the preorder traversal (index tracked globally) and create a node with that value.
- We find the index of that value in the inorder traversal using a hashmap for O(1) lookups. This is the mid point of the left and right subtrees.
- We recursively set the left child of the node to be the result of calling DFS on the left and mid - 1.
- We recursively set the right child of the node to be the result of calling DFS on the mid + 1 and right.

Finally, we call the DFS function with the initial range of 0 and n - 1, where n is the length of the inorder traversal.

## Complexity
- Time: `O(n)`, we visit each node once.
- Space: `O(n)`, the hashmap takes `O(n)` space and the recursion stack takes `O(n)` space.
