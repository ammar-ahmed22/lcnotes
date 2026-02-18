## Intuition
We need removal from anywhere and insertion at either end to all be O(1). Thus, we can use a hashmap with a doubly-linked list.

## Implementation
In a nutshell, we store list nodes by key in a hashmap as well as keep track of our doubly-linked list with head and tail pointers. 

On `get`, we check if the node exists, if it does, we disconnect (remove) that node from the list and add it to the most-recently used (MRU) end which we can define as the tail. Both of these operations can be done in O(1) time as it is doubly-linked and the node is stored in a hashmap. If the node doesn't exist, simply return -1.

On `put`, we check if the node exists, it it does, we update the value stored in the node. Then we disconnect (remove) that node from the list and add it to the MRU end. If it does not exist, we create a new node, add it to the hashmap, and then add the node to the MRU end. After this, we check if the length of our hashmap exceeds the capacity (need to evict), if so, we remove the node at the head of the list (LRU end), and delete the node from the hashmap using the key stored in the node.

## Edge-cases
To remove a bunch of edge-cases, we can use sentinel (dummy) nodes at the head and tail so that we don't have to deal with many null pointer checks. This makes removals and insertions quite trivial.

We should also ensure to store the key as well as the value in the list node so that we can easily delete the node from the hashmap on eviction.

## Complexity
- Time: `O(1)`: Since we use a hashmap to store nodes and a doubly-linked list, node lookup is `O(1)`, removal is `O(1)`, insertion is `O(1)`
- Space: `O(n)`: where `n` is the capacity. At most we store the `n` nodes as they get evicted when capacity is reached.
