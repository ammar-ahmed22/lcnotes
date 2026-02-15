## Intuition
With a sorted array, we can leverage binary search. For each number, its complement (`target - curr`) must be in the sorted subarray to its right, making binary search an efficient lookup method.

## Implementation
Iterate through the array. For each element, calculate its complement and perform binary search on the elements to the right. If found, return the 1-indexed pair. If not found, continue to the next element.

## Edge-cases
The problem guarantees exactly one solution exists, so we don't need to handle the case of no valid pair. Remember to return 1-based indices as required.

## Complexity
- Time: `O(n log n)` — binary search for each element
- Space: `O(1)` — only tracking pointers
