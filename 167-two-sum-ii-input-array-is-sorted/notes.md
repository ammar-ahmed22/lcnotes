## Intuition
The sorted property allows us to use binary search. For each number, its complement (target - current) must be somewhere to its right (since using the same element twice isn't allowed and left elements are smaller).

## Implementation
For each element at index i, compute the complement and binary search for it in the subarray from i+1 to the end. If found, return both indices (1-indexed as per the problem). If not found, continue to the next element.

## Edge-cases
Remember to return 1-indexed results as required by the problem.

## Complexity
Time `O(n log n)` for n binary searches. Space `O(1)` using only pointers.
