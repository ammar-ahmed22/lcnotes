## Intuition
We want to take the smallest value at a time from each list and only iterate further on that list after a value is taken from that list.

## Implementation
We can use a min-heap alongside keeping track of the pointers in array and accessing them via index. To start, we create our array of pointers to the lists. At the same time, we add the first element of each non-empty list to the heap along with its index (with the value as the priority).

After this, we iterate while the heap is not empty, we pop from the heap and add the new node to our resultant list. Using the index, we increment that specific pointer. Then, we check if the the updated pointer is not null (i.e. next is defined) and we push that value and its index to the heap. This will also ensure that whichever index is popped from the heap will be defined at that point.

Finally, return the result.

## Edge-cases
Ensure to push the first elements from the non-empty lists from the heap to start so that we have something to iterate over.

## Complexity
- Time: `O(N log k)`: where `N` is the total number of nodes in all `k` lists. The main iteration is the heap iteration which will run once for each node in the result, on each iteration, we pop and potentially push to the heap which is `O(log k)` because the size of the heap will never exceed the starting size will be at most `k`.
- Space: `O(k)`: The only extra space is the heap which will have, at most, `k` elements
