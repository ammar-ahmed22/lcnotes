## Intuition
Maintaining a min heap of length `k` will keep the `kth` largest elements in it. If the min heap exceeds length `k`, the smallest of `k` seen, will be removed, maintaining the `kth` largest.

## Implementation
Initialize a min heap.

Iterate over the numbers:
- Add the number to the min heap
- If the heap exceeds length `k`, pop from the heap

Return the root of the heap

## Complexity
- Time: `O(n log k)`, we iterate over the numbers once and the heap operations are worst-case `O(log k)` because the heap maintains a length of `k`.
- Space: `O(k)`, The max size of the heap is `O(k)`.
