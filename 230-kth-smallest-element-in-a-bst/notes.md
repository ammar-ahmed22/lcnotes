## Intuition
Inorder traversal of a BST provides values in sorted, ascending order.

## Implementation
Define a global variable, `count`, that will count the values seen in the inorder traversal. Define another global variable for the result. 

Define a recursive function for the inorder traversal:
- If the node is null, return early
- Recurse on the left node
- Increment the `count`
- If `count == k`, update the result and return early
- Recurse on the right node

Call the recursive function on the root and return the result.

## Edge-cases
Important to return early after updating the result to ensure we don't process unnecessary nodes.

## Complexity
- Time: `O(h)`, where `h` is the height of the BST. At the worst-case, we will only traverse the height of the BST.
- Spec: `O(h)`, where `h` is the height of the BST. Due to the recursive call stack.
